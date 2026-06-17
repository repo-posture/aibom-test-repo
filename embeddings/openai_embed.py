from openai import OpenAI

client = OpenAI()

# Models: text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002


def embed_small(text: str) -> list[float]:
    return client.embeddings.create(input=text, model="text-embedding-3-small").data[0].embedding


def embed_large(text: str) -> list[float]:
    return client.embeddings.create(input=text, model="text-embedding-3-large").data[0].embedding


def embed_ada(text: str) -> list[float]:
    return client.embeddings.create(input=text, model="text-embedding-ada-002").data[0].embedding
