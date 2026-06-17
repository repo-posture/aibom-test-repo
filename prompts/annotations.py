from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# langchain-core Library (2 occurrences) + LangChain via langchain_core
# Covers: AIBOM-09 (LangChain Framework via langchain_core), AIBOM-10 (Library type component)

annotation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You annotate text with named entities."),
        ("human", "Annotate the following: {text}"),
    ]
)

parser = StrOutputParser()

annotation_chain = annotation_prompt | parser
