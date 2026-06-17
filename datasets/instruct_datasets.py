from datasets import load_dataset

# Datasets: HuggingFaceH4/ultrafeedback_binarized, databricks/databricks-dolly-15k,
#           tatsu-lab/alpaca, OpenAssistant/oasst1

ULTRAFEEDBACK = "HuggingFaceH4/ultrafeedback_binarized"
DOLLY = "databricks/databricks-dolly-15k"
ALPACA = "tatsu-lab/alpaca"
OASST = "OpenAssistant/oasst1"


def load_ultrafeedback(split: str = "train_prefs"):
    return load_dataset(ULTRAFEEDBACK, split=split)


def load_dolly():
    return load_dataset(DOLLY)


def load_alpaca():
    return load_dataset(ALPACA)


def load_oasst():
    return load_dataset(OASST)
