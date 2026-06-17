from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

# HuggingFace Datasets (2 Dataset components) + openai-community/gpt2 Model
# Covers: AIBOM-12 (dataset detection), AIBOM-15/18 (Type=Dataset filter), AIBOM-07 (HF model via transformers)

FEEDBACK_DATASET = "HuggingFaceH4/ultrafeedback_binarized"
CODE_DATASET = "bigcode/starcoderdata"
GPT2_MODEL = "openai-community/gpt2"


def load_feedback_data(split: str = "train_prefs"):
    return load_dataset(FEEDBACK_DATASET, split=split)


def load_code_data(split: str = "train"):
    return load_dataset(CODE_DATASET, split=split)


def load_gpt2():
    tokenizer = AutoTokenizer.from_pretrained(GPT2_MODEL)
    model = AutoModelForCausalLM.from_pretrained(GPT2_MODEL)
    return tokenizer, model
