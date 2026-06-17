# AIBOM Test Repository

A repository demonstrating usage of major AI/ML providers, orchestration frameworks, embedding models, and training datasets across Python and JavaScript.

## Structure

```
aibom-test-repo/
├── chatmodels/
│   ├── openai_chat.py          — gpt-4o, gpt-4, gpt-3.5-turbo
│   ├── anthropic_chat.py       — claude-3-5-sonnet, claude-3-opus, claude-3-haiku
│   ├── google_chat.py          — gemini-1.5-pro, gemini-1.5-flash, gemini-pro
│   ├── cohere_chat.py          — command-r-plus, command-r, command
│   └── mistral_chat.py         — mistral-large, mistral-small, open-mixtral-8x7b
├── frameworks/
│   ├── langchain_app.py        — LangChain + langchain-core + multi-provider chains
│   ├── langgraph_app.py        — LangGraph multi-agent orchestration
│   ├── llamaindex_app.py       — LlamaIndex RAG with HuggingFace + OpenAI
│   ├── haystack_app.py         — Haystack RAG pipeline (OpenAI + Anthropic + Gemini)
│   └── crewai_app.py           — CrewAI multi-agent crew (OpenAI + Anthropic + Gemini)
├── embeddings/
│   ├── openai_embed.py         — text-embedding-3-small/large, text-embedding-ada-002
│   ├── hf_embed.py             — all-MiniLM-L6-v2, BAAI/bge-large-en-v1.5, intfloat/e5-large-v2
│   └── cohere_google_embed.py  — embed-english-v3.0, embed-multilingual-v3.0, text-embedding-004
├── hf_models/
│   ├── generation.py           — Llama-2-7b, Mistral-7B-v0.1, falcon-7b
│   ├── text2text.py            — flan-t5-large, bart-large-cnn, opus-mt-en-de
│   └── reasoning.py            — DeepSeek-R1, Qwen2-7B-Instruct, gpt2
├── datasets/
│   ├── instruct_datasets.py    — ultrafeedback_binarized, dolly-15k, alpaca, oasst1
│   ├── code_datasets.py        — starcoderdata, github-code, openai_humaneval
│   └── nlp_datasets.py         — squad, imdb, ai2_arc, hh-rlhf, boolq
├── edge_cases/
│   └── onnx_local.py           — Local ONNX model (non-HuggingFace)
└── js/
    ├── openai_client.js        — gpt-4o, gpt-4, gpt-3.5-turbo, text-embedding-3-small/large
    └── anthropic_client.js     — claude-3-5-sonnet, claude-3-opus, claude-3-haiku
```

## AI Components Summary

### Frameworks
| Framework | Library | Files |
|---|---|---|
| LangChain | `langchain`, `langchain-core` | `frameworks/langchain_app.py` |
| LangGraph | `langgraph` | `frameworks/langgraph_app.py` |
| LlamaIndex | `llama-index-core` | `frameworks/llamaindex_app.py` |
| Haystack | `haystack-ai` | `frameworks/haystack_app.py` |
| CrewAI | `crewai` | `frameworks/crewai_app.py` |

### Libraries
| Library | Provider |
|---|---|
| `langchain-core`, `langchain-anthropic`, `langchain-google-genai`, `langchain-cohere`, `langchain-huggingface` | Various |
| `llama-index-llms-openai`, `llama-index-llms-anthropic`, `llama-index-embeddings-huggingface` | Various |
| `openai`, `anthropic`, `google-generativeai`, `cohere`, `mistralai` | OpenAI / Anthropic / Google / Cohere / Mistral |
| `transformers`, `sentence-transformers` | HuggingFace |

### Models
| Model | Type | Provider |
|---|---|---|
| gpt-4o, gpt-4, gpt-3.5-turbo | Model | OpenAI |
| text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002 | Model | OpenAI |
| claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-haiku-20240307 | Model | Anthropic |
| gemini-1.5-pro, gemini-1.5-flash, gemini-pro | Model | Google |
| text-embedding-004 | Model | Google |
| command-r-plus, command-r, command | Model | Cohere |
| embed-english-v3.0, embed-multilingual-v3.0 | Model | Cohere |
| mistral-large-latest, mistral-small-latest, open-mixtral-8x7b | Model | Mistral |
| meta-llama/Llama-2-7b-hf | Model | HuggingFace |
| mistralai/Mistral-7B-v0.1 | Model | HuggingFace |
| tiiuae/falcon-7b | Model | HuggingFace |
| deepseek-ai/DeepSeek-R1 | Model | HuggingFace |
| Qwen/Qwen2-7B-Instruct | Model | HuggingFace |
| google/flan-t5-large | Model | HuggingFace |
| facebook/bart-large-cnn | Model | HuggingFace |
| Helsinki-NLP/opus-mt-en-de | Model | HuggingFace |
| sentence-transformers/all-MiniLM-L6-v2 | Model | HuggingFace |
| BAAI/bge-large-en-v1.5 | Model | HuggingFace |
| intfloat/e5-large-v2 | Model | HuggingFace |
| openai-community/gpt2 | Model | HuggingFace |

### Datasets
| Dataset | Provider |
|---|---|
| HuggingFaceH4/ultrafeedback_binarized | HuggingFace |
| databricks/databricks-dolly-15k | HuggingFace |
| tatsu-lab/alpaca | HuggingFace |
| OpenAssistant/oasst1 | HuggingFace |
| bigcode/starcoderdata | HuggingFace |
| codeparrot/github-code | HuggingFace |
| openai/openai_humaneval | HuggingFace |
| squad | HuggingFace |
| imdb | HuggingFace |
| allenai/ai2_arc | HuggingFace |
| Anthropic/hh-rlhf | HuggingFace |
| google/boolq | HuggingFace |

## Setup

```bash
pip install -r requirements.txt
```
