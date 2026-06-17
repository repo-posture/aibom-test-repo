import langchain
from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain import LLMChain, PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Framework: LangChain
# Libraries: langchain-core, langchain-anthropic, langchain-google-genai, langchain-cohere

llm_openai = ChatOpenAI(model="gpt-4o")
llm_claude = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_cohere = ChatCohere(model="command-r-plus")

prompt = ChatPromptTemplate.from_messages([("human", "{question}")])
parser = StrOutputParser()

openai_chain = prompt | llm_openai | parser
claude_chain = prompt | llm_claude | parser
gemini_chain = prompt | llm_gemini | parser
cohere_chain = prompt | llm_cohere | parser
