from transformers import (
    T5ForConditionalGeneration,
    T5Tokenizer,
    BartForConditionalGeneration,
    BartTokenizer,
    pipeline,
)

# Models: google/flan-t5-large, facebook/bart-large-cnn, Helsinki-NLP/opus-mt-en-de

FLAN_T5 = "google/flan-t5-large"
BART = "facebook/bart-large-cnn"
OPUS_MT = "Helsinki-NLP/opus-mt-en-de"


def load_flan_t5():
    tokenizer = T5Tokenizer.from_pretrained(FLAN_T5)
    model = T5ForConditionalGeneration.from_pretrained(FLAN_T5)
    return tokenizer, model


def load_bart_summarizer():
    tokenizer = BartTokenizer.from_pretrained(BART)
    model = BartForConditionalGeneration.from_pretrained(BART)
    return tokenizer, model


def load_translator():
    return pipeline("translation", model=OPUS_MT)
