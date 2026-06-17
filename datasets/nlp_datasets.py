from datasets import load_dataset

# Datasets: squad, imdb, allenai/ai2_arc, Anthropic/hh-rlhf, google/boolq

SQUAD = "squad"
IMDB = "imdb"
ARC = "allenai/ai2_arc"
HH_RLHF = "Anthropic/hh-rlhf"
BOOLQ = "google/boolq"


def load_squad():
    return load_dataset(SQUAD)


def load_imdb():
    return load_dataset(IMDB)


def load_arc():
    return load_dataset(ARC, "ARC-Challenge")


def load_hh_rlhf():
    return load_dataset(HH_RLHF)


def load_boolq():
    return load_dataset(BOOLQ)
