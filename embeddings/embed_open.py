from openai import OpenAI
from sentence_transformers import SentenceTransformer

# openai Library + text-embedding-3-small Model + sentence-transformers/all-MiniLM-L6-v2 Model
# Covers: AIBOM-07 (HuggingFace model), AIBOM-08 (text-embedding-3-small), AIBOM-10 (multi-type)
# Detail drawer: sentence-transformers/all-MiniLM-L6-v2 — verify Model Card link + Datasets shown

client = OpenAI()

HF_EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OPENAI_EMBED_MODEL = "text-embedding-3-small"


def embed_with_openai(text: str) -> list[float]:
    response = client.embeddings.create(input=text, model=OPENAI_EMBED_MODEL)
    return response.data[0].embedding


def embed_with_hf(texts: list[str]) -> list:
    model = SentenceTransformer(HF_EMBED_MODEL)
    return model.encode(texts).tolist()
