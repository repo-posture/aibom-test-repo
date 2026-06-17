# AIBOM Test Repository

This repository is purpose-built to test Harness SSCA's **AI BOM (AIBOM)** feature.
Each file is crafted to trigger specific AIBOM test scenarios from the test plan (SSCA-4123).

---

## Repository Structure

```
aibom-test-repo/
├── chatmodels/
│   ├── chat_model.py       → LangChain (1) + gpt-4 (1)
│   └── hugging_face.py     → LangChain (2) + langchain-huggingface (1) + sentence-transformers/all-MiniLM-L6-v2 (1)
├── prompts/
│   ├── prompts.py          → LangChain (4 occurrences in one file)
│   ├── chatbot.py          → LangChain (1) + gpt-4 (1)
│   ├── chains.py           → LangChain (1) + gpt-4 (1)
│   └── annotations.py      → langchain-core (2)
├── embeddings/
│   ├── embed_open.py       → openai (1) + text-embedding-3-small (1) + sentence-transformers/all-MiniLM-L6-v2 (1)
│   └── hf_embeddings.py    → langchain-huggingface (1) + transformers (1) + sentence-transformers/all-MiniLM-L6-v2 (1)
├── datasets/
│   └── data_loader.py      → HuggingFaceH4/ultrafeedback_binarized (1) + bigcode/starcoderdata (1) + openai-community/gpt2 (1)
├── generative/
│   └── google_model.py     → google-generativeai (1) + gpt-4 (1)
├── edge_cases/
│   └── onnx_local.py       → ONNX local model (non-HuggingFace, edge case)
├── js/
│   └── ai_client.js        → gpt-4 (JS) + text-embedding-3-small (JS)
└── requirements.txt
```

---

## Expected AIBOM Components

| Component | Type | Provider | Expected Occurrences | Files |
|---|---|---|---|---|
| LangChain | Framework | LangChain | 9+ | chat_model.py, hugging_face.py, prompts.py(×4), chatbot.py, chains.py, annotations.py |
| langchain-core | Library | Unknown | 2 | annotations.py |
| langchain-huggingface | Library | HuggingFace | 2 | hugging_face.py, hf_embeddings.py |
| openai | Library | OpenAI | 2 | embed_open.py, generative/google_model.py |
| transformers | Library | HuggingFace | 1 | hf_embeddings.py |
| google-generativeai | Library | Google | 1 | google_model.py |
| gpt-4 | Model | OpenAI | 4 | chat_model.py, chatbot.py, chains.py, google_model.py |
| text-embedding-3-small | Model | OpenAI | 2 | embed_open.py, js/ai_client.js |
| sentence-transformers/all-MiniLM-L6-v2 | Model | HuggingFace | 3 | hugging_face.py, embed_open.py, hf_embeddings.py |
| openai-community/gpt2 | Model | HuggingFace | 1 | data_loader.py |
| HuggingFaceH4/ultrafeedback_binarized | Dataset | HuggingFace | 1 | data_loader.py |
| bigcode/starcoderdata | Dataset | HuggingFace | 1 | data_loader.py |

---

## Test Scenario Coverage

### B. AI Model Detection

| Scenario | What to verify | File(s) |
|---|---|---|
| AIBOM-07 | HuggingFace model detected | `embeddings/embed_open.py`, `embeddings/hf_embeddings.py` |
| AIBOM-08 | OpenAI models: gpt-4 (4×), text-embedding-3-small (2×) | `chatmodels/`, `prompts/`, `generative/`, `js/` |
| AIBOM-09 | LangChain detected as Framework | `chatmodels/`, `prompts/` |
| AIBOM-10 | All 4 types present: Model, Library, Framework, Dataset | Full repo scan |
| AIBOM-11 | LangChain has 9+ occurrences across 7 files; gpt-4 has 4 occurrences | LangChain → click component → check Occurrences drawer |
| AIBOM-12 | 2 datasets detected: ultrafeedback_binarized + starcoderdata | `datasets/data_loader.py` |

### C. AIBOM Viewer — UI

| Scenario | What to verify | Expected |
|---|---|---|
| AIBOM-14 | Columns visible | Component, Type, Provider, PURL, Occurrences |
| AIBOM-15 | Filter by Model | gpt-4, text-embedding-3-small, sentence-transformers/all-MiniLM-L6-v2, openai-community/gpt2 |
| AIBOM-16 | Filter by Library | langchain-core, langchain-huggingface, openai, transformers, google-generativeai |
| AIBOM-17 | Filter by Framework | LangChain |
| AIBOM-18 | Filter by Dataset | HuggingFaceH4/ultrafeedback_binarized, bigcode/starcoderdata |
| AIBOM-19 | Filter by Agent | Empty state (no agents in this repo) |
| AIBOM-21 | PURL format for HuggingFace model | `pkg:huggingface/sentence-transformers/all-MiniLM-L6-v2@<commit>` |

### Detail Drawer (new — from component row click)

| Click on | What to verify in the drawer |
|---|---|
| **LangChain** (Framework) | Details: Name=LangChain, Type=Framework, Provider=LangChain, PURL=pkg:pypi/langchain. Occurrences section: lists each file with its per-file count. No Model Card or Datasets section. |
| **sentence-transformers/all-MiniLM-L6-v2** (Model, HuggingFace) | Details: Type=Model, Provider=HuggingFace, PURL=pkg:huggingface/... **Model Card** section: link to https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2. **Datasets** section: training dataset tags (s2orc, ms_marco, etc.). Occurrences: 3 files (hugging_face.py, embed_open.py, hf_embeddings.py). |
| **gpt-4** (Model, OpenAI) | Details: Type=Model, Provider=OpenAI. **No Model Card** section (not HuggingFace). **No Datasets** section. Occurrences: 4 files. |
| **google-generativeai** (Library, Google) | Details: Type=Library, Provider=Google, PURL=pkg:pypi/google-generativeai. Occurrences: 1 file (google_model.py). |
| **HuggingFaceH4/ultrafeedback_binarized** (Dataset) | Details: Type=Dataset, Provider=HuggingFace. Occurrences: 1 file (data_loader.py). |

### E. Edge Cases

| Scenario | What to verify | File |
|---|---|---|
| AIBOM-30 | ONNX local model detected in viewer; but CycloneDX download shows error since it is not a HuggingFace model | `edge_cases/onnx_local.py` |
| AIBOM-27 | Use a different repo/branch with no AI imports | Scan any plain Python repo without AI libraries |
| AIBOM-19 | Agent filter shows empty state | No agents present in this repo |

---

## Pipeline Step Configuration

Use the following values when adding the AIBOM Generation step in Harness:

| Field | Value |
|---|---|
| Repository URL | `https://github.com/<your-org>/aibom-test-repo` |
| Git Branch | `main` |
| AIBOM Format | CycloneDX |
| Source Path | *(leave blank to scan full repo)* |

To test **AIBOM-04** (Source Path scoping), set Source Path to `embeddings/` — only embedding-related models should appear.

To test **AIBOM-05** (Additional CLI Flags), add `--verbose` and verify verbose scanner output in pipeline logs.
# aibom-test-repo
