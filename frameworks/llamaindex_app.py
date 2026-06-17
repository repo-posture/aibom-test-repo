from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI as LlamaOpenAI
from llama_index.llms.anthropic import Anthropic as LlamaAnthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding

# Framework: llama-index-core
# Libraries: llama-index-llms-openai, llama-index-llms-anthropic, llama-index-embeddings-huggingface, llama-index-embeddings-openai
# Models: gpt-4o, claude-3-5-sonnet-20241022, BAAI/bge-large-en-v1.5, text-embedding-3-small

Settings.llm = LlamaOpenAI(model="gpt-4o")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")

claude_llm = LlamaAnthropic(model="claude-3-5-sonnet-20241022")
openai_embed = OpenAIEmbedding(model="text-embedding-3-small")


def build_index(data_dir: str) -> VectorStoreIndex:
    docs = SimpleDirectoryReader(data_dir).load_data()
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    return VectorStoreIndex.from_documents(docs, transformations=[splitter])


def query_index(index: VectorStoreIndex, question: str) -> str:
    engine = index.as_query_engine()
    return str(engine.query(question))
