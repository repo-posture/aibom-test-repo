from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# LangChain (1 occurrence) + gpt-4 (1 occurrence)
# Covers: AIBOM-08 (gpt-4 occurrence 3 of 4), AIBOM-09 (LangChain)

llm = ChatOpenAI(model="gpt-4")

step1_prompt = PromptTemplate(
    template="Extract the key facts from: {text}",
    input_variables=["text"],
)
step2_prompt = PromptTemplate(
    template="Given these facts: {facts}\nWrite a brief report.",
    input_variables=["facts"],
)

chain1 = LLMChain(llm=llm, prompt=step1_prompt, output_key="facts")
chain2 = LLMChain(llm=llm, prompt=step2_prompt, output_key="report")

pipeline = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["text"],
    output_variables=["report"],
)
