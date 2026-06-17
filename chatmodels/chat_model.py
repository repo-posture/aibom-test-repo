from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate

# LangChain + gpt-4
# Covers: AIBOM-09 (LangChain Framework), AIBOM-08 (gpt-4 Model), AIBOM-10 (multi-type)

llm = ChatOpenAI(model="gpt-4", temperature=0)

prompt = PromptTemplate(
    template="You are a helpful assistant. Answer the question: {question}",
    input_variables=["question"],
)

chain = LLMChain(llm=llm, prompt=prompt)


def ask(question: str) -> str:
    return chain.run(question=question)
