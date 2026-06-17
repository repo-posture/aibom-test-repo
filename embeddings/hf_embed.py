from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel
import torch

# Models: sentence-transformers/all-MiniLM-L6-v2, BAAI/bge-large-en-v1.5, intfloat/e5-large-v2

MINILM = "sentence-transformers/all-MiniLM-L6-v2"
BGE = "BAAI/bge-large-en-v1.5"
E5 = "intfloat/e5-large-v2"


def embed_minilm(texts: list[str]) -> list:
    model = SentenceTransformer(MINILM)
    return model.encode(texts).tolist()


def embed_bge(texts: list[str]) -> list:
    model = SentenceTransformer(BGE)
    return model.encode(texts, normalize_embeddings=True).tolist()


def embed_e5(texts: list[str]) -> torch.Tensor:
    tokenizer = AutoTokenizer.from_pretrained(E5)
    model = AutoModel.from_pretrained(E5)
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)
