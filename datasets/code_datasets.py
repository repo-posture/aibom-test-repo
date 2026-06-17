from datasets import load_dataset

# Datasets: bigcode/starcoderdata, codeparrot/github-code, openai/openai_humaneval

STARCODER = "bigcode/starcoderdata"
GITHUB_CODE = "codeparrot/github-code"
HUMANEVAL = "openai/openai_humaneval"


def load_starcoder(split: str = "train"):
    return load_dataset(STARCODER, split=split)


def load_github_code():
    return load_dataset(GITHUB_CODE)


def load_humaneval():
    return load_dataset(HUMANEVAL)
