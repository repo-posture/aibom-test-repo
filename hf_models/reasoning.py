from transformers import AutoModelForCausalLM, AutoTokenizer

# Models: deepseek-ai/DeepSeek-R1, Qwen/Qwen2-7B-Instruct, openai-community/gpt2

DEEPSEEK_R1 = "deepseek-ai/DeepSeek-R1"
QWEN2 = "Qwen/Qwen2-7B-Instruct"
GPT2 = "openai-community/gpt2"


def load_deepseek():
    tokenizer = AutoTokenizer.from_pretrained(DEEPSEEK_R1)
    model = AutoModelForCausalLM.from_pretrained(DEEPSEEK_R1, trust_remote_code=True)
    return tokenizer, model


def load_qwen():
    tokenizer = AutoTokenizer.from_pretrained(QWEN2)
    model = AutoModelForCausalLM.from_pretrained(QWEN2)
    return tokenizer, model


def load_gpt2():
    tokenizer = AutoTokenizer.from_pretrained(GPT2)
    model = AutoModelForCausalLM.from_pretrained(GPT2)
    return tokenizer, model
