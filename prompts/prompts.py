import langchain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate

# LangChain (4 occurrences in this file)
# Covers: AIBOM-09 (LangChain Framework), AIBOM-11 (high occurrence count per file)

SYSTEM_INSTRUCTION = langchain.prompts.SystemMessagePromptTemplate.from_template(
    "You are a helpful assistant that answers questions clearly and concisely."
)

qa_prompt = PromptTemplate(
    template="Context:\n{context}\n\nQuestion: {question}\nAnswer:",
    input_variables=["context", "question"],
)

summarize_prompt = PromptTemplate(
    template="Summarize the following text in 2-3 sentences:\n\n{text}",
    input_variables=["text"],
)

classify_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You classify text sentiment."),
        ("human", "Classify the sentiment of: {text}"),
    ]
)
