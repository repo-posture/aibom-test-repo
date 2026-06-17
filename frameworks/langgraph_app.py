import langchain
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_core.messages import HumanMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from typing import TypedDict, Annotated
import operator

# Framework: LangGraph
# Libraries: langchain-core, langchain-anthropic
# Models: gpt-4o (orchestrator), claude-3-5-sonnet-20241022 (worker)


class AgentState(TypedDict):
    messages: Annotated[list, operator.add]


orchestrator = ChatOpenAI(model="gpt-4o")
worker = ChatAnthropic(model="claude-3-5-sonnet-20241022")


def orchestrator_node(state: AgentState) -> AgentState:
    response = orchestrator.invoke(state["messages"])
    return {"messages": [response]}


def worker_node(state: AgentState) -> AgentState:
    response = worker.invoke(state["messages"])
    return {"messages": [response]}


def router(state: AgentState) -> str:
    last = state["messages"][-1]
    return "worker" if "delegate" in last.content.lower() else END


graph = StateGraph(AgentState)
graph.add_node("orchestrator", orchestrator_node)
graph.add_node("worker", worker_node)
graph.set_entry_point("orchestrator")
graph.add_conditional_edges("orchestrator", router)
graph.add_edge("worker", END)

app = graph.compile()
