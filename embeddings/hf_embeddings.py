from langchain_huggingface import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModel
import torch

# langchain-huggingface Library + transformers Library + HuggingFace model
# Covers: AIBOM-07 (HuggingFace model via transformers), AIBOM-09 (LangChain), AIBOM-10 (multi-type)

MINILM_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_langchain_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(model_name=MINILM_MODEL)


def get_raw_hf_embeddings(texts: list[str]) -> torch.Tensor:
    tokenizer = AutoTokenizer.from_pretrained(MINILM_MODEL)
    model = AutoModel.from_pretrained(MINILM_MODEL)
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)
