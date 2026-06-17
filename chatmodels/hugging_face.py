import langchain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# LangChain (2 occurrences here) + langchain-huggingface Library + HuggingFace Model
# Covers: AIBOM-09 (LangChain Framework), AIBOM-07 (HuggingFace model), AIBOM-11 (occurrences)

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(model_name=EMBED_MODEL)


def build_vector_store(texts: list[str]) -> FAISS:
    embeddings = get_embeddings()
    return FAISS.from_texts(texts, embeddings)
