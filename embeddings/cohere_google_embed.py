import cohere
import google.generativeai as genai

co = cohere.Client()
genai.configure(api_key="GOOGLE_API_KEY")

# Cohere Models: embed-english-v3.0, embed-multilingual-v3.0
# Google Models: text-embedding-004


def embed_cohere_en(texts: list[str]) -> list:
    response = co.embed(texts=texts, model="embed-english-v3.0", input_type="search_document")
    return response.embeddings


def embed_cohere_multilingual(texts: list[str]) -> list:
    response = co.embed(texts=texts, model="embed-multilingual-v3.0", input_type="search_document")
    return response.embeddings


def embed_google(text: str) -> list[float]:
    result = genai.embed_content(model="text-embedding-004", content=text)
    return result["embedding"]
