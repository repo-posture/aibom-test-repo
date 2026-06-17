from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Models: meta-llama/Llama-2-7b-hf, mistralai/Mistral-7B-v0.1, tiiuae/falcon-7b

LLAMA2 = "meta-llama/Llama-2-7b-hf"
MISTRAL_7B = "mistralai/Mistral-7B-v0.1"
FALCON = "tiiuae/falcon-7b"


def load_llama2():
    tokenizer = AutoTokenizer.from_pretrained(LLAMA2)
    model = AutoModelForCausalLM.from_pretrained(LLAMA2)
    return tokenizer, model


def load_mistral():
    return pipeline("text-generation", model=MISTRAL_7B)


def load_falcon():
    return pipeline("text-generation", model=FALCON)
