from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI

# LangChain (1 occurrence) + gpt-4 (1 occurrence)
# Covers: AIBOM-08 (gpt-4 occurrence 2 of 4), AIBOM-09 (LangChain)

memory = ConversationBufferMemory()

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

conversation = ConversationChain(llm=llm, memory=memory, verbose=False)


def chat(user_input: str) -> str:
    return conversation.predict(input=user_input)
