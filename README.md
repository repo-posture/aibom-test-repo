# AIBOM Test Repository

A minimal repository demonstrating usage of popular AI/ML frameworks and models across Python and JavaScript. Used for validating AI Bill of Materials (AIBOM) generation in CI/CD pipelines.

## Structure

```
aibom-test-repo/
├── chatmodels/
│   ├── chat_model.py       — LangChain chain with OpenAI GPT-4
│   └── hugging_face.py     — LangChain + HuggingFace embeddings
├── prompts/
│   ├── prompts.py          — LangChain prompt templates
│   ├── chatbot.py          — Conversational chain with memory
│   ├── chains.py           — Sequential LangChain pipeline
│   └── annotations.py      — langchain-core output parsing
├── embeddings/
│   ├── embed_open.py       — OpenAI + sentence-transformers embeddings
│   └── hf_embeddings.py    — HuggingFace Transformers embeddings
├── datasets/
│   └── data_loader.py      — HuggingFace datasets + GPT-2
├── generative/
│   └── google_model.py     — Google Gemini + OpenAI GPT-4
├── edge_cases/
│   └── onnx_local.py       — Local ONNX model inference
├── js/
│   └── ai_client.js        — OpenAI SDK (Node.js)
└── requirements.txt
```

## AI Components Used

| Component | Type | Provider |
|---|---|---|
| LangChain | Framework | LangChain |
| langchain-core | Library | — |
| langchain-huggingface | Library | HuggingFace |
| openai | Library | OpenAI |
| transformers | Library | HuggingFace |
| google-generativeai | Library | Google |
| gpt-4 | Model | OpenAI |
| text-embedding-3-small | Model | OpenAI |
| sentence-transformers/all-MiniLM-L6-v2 | Model | HuggingFace |
| openai-community/gpt2 | Model | HuggingFace |
| HuggingFaceH4/ultrafeedback_binarized | Dataset | HuggingFace |
| bigcode/starcoderdata | Dataset | HuggingFace |

## Setup

```bash
pip install -r requirements.txt
```
