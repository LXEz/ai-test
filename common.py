import os

from langchain_chroma import Chroma
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings import OllamaEmbeddings


default_llm = "qwen2.5:72b"
base_ollama_url = "http://gpt:11434"
_model = None
_ollama_embedding = None
_vector_store = None


def set_langsmith_env():
    lang_smith_api_key = "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"
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = lang_smith_api_key


def get_vector_store():
    global _vector_store
    if _vector_store is None:
        _vector_store = Chroma(
            embedding_function=get_embedding(), persist_directory="chroma_db"
        )
    return _vector_store


def get_llm():
    global _model
    if _model is None:
        _model = Ollama(model=default_llm, base_url=base_ollama_url)
    return _model


def get_embedding():
    global _ollama_embedding
    if _ollama_embedding is None:
        _ollama_embedding = OllamaEmbeddings(
            model=default_llm, base_url=base_ollama_url, show_progress=True
        )
    return _ollama_embedding


set_langsmith_env()
