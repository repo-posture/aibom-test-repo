from haystack import Pipeline
from haystack.components.generators import OpenAIGenerator
from haystack.components.builders import PromptBuilder
from haystack.components.retrievers.in_memory import InMemoryBM25Retriever
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack_integrations.components.generators.anthropic import AnthropicGenerator
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator

# Framework: haystack-ai
# Libraries: haystack-integrations (anthropic, google-ai)
# Models: gpt-4o, claude-3-5-sonnet-20241022, gemini-1.5-pro

document_store = InMemoryDocumentStore()

openai_gen = OpenAIGenerator(model="gpt-4o")
anthropic_gen = AnthropicGenerator(model="claude-3-5-sonnet-20241022")
gemini_gen = GoogleAIGeminiGenerator(model="gemini-1.5-pro")

prompt_builder = PromptBuilder(
    template="Given context: {{documents}}\nAnswer: {{question}}"
)

rag_pipeline = Pipeline()
rag_pipeline.add_component("retriever", InMemoryBM25Retriever(document_store=document_store))
rag_pipeline.add_component("prompt", prompt_builder)
rag_pipeline.add_component("llm", openai_gen)
rag_pipeline.connect("retriever", "prompt.documents")
rag_pipeline.connect("prompt", "llm")
