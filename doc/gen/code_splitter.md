```python
from common import get_llm, get_embedding,get_vector_store

model = get_llm()
ollama_embedding = get_embedding()
vector_store = get_vector_store()
```

读取本地python文件


```python
from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)


with open("common.py", "r", encoding="utf-8") as f:
    PYTHON_CODE = f.read()


python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
python_docs
```




    [Document(metadata={}, page_content='import os'),
     Document(metadata={}, page_content='from langchain_chroma import Chroma'),
     Document(metadata={}, page_content='from langchain_community.llms.ollama import'),
     Document(metadata={}, page_content='Ollama'),
     Document(metadata={}, page_content='from langchain_community.embeddings import'),
     Document(metadata={}, page_content='OllamaEmbeddings'),
     Document(metadata={}, page_content='default_llm = "qwen2.5:72b"'),
     Document(metadata={}, page_content='base_ollama_url = "http://gpt:11434"'),
     Document(metadata={}, page_content='_model = None\n_ollama_embedding = None'),
     Document(metadata={}, page_content='_vector_store = None'),
     Document(metadata={}, page_content='def set_langsmith_env():'),
     Document(metadata={}, page_content='lang_smith_api_key ='),
     Document(metadata={}, page_content='"lsv2_pt_de8e0f31d1dd4bc7af7a6b8a66c6af6c_014993d'),
     Document(metadata={}, page_content='20f"'),
     Document(metadata={}, page_content='os.environ["LANGCHAIN_TRACING_V2"] = "true"'),
     Document(metadata={}, page_content='os.environ["LANGCHAIN_API_KEY"] ='),
     Document(metadata={}, page_content='lang_smith_api_key'),
     Document(metadata={}, page_content='def get_vector_store():\n    global _vector_store'),
     Document(metadata={}, page_content='if _vector_store is None:'),
     Document(metadata={}, page_content='_vector_store = Chroma('),
     Document(metadata={}, page_content='embedding_function=get_embedding(),'),
     Document(metadata={}, page_content='persist_directory="chroma_db"'),
     Document(metadata={}, page_content=')\n    return _vector_store'),
     Document(metadata={}, page_content='def get_llm():\n    global _model'),
     Document(metadata={}, page_content='if _model is None:'),
     Document(metadata={}, page_content='_model = Ollama(model=default_llm,'),
     Document(metadata={}, page_content='base_url=base_ollama_url)'),
     Document(metadata={}, page_content='return _model'),
     Document(metadata={}, page_content='def get_embedding():\n    global _ollama_embedding'),
     Document(metadata={}, page_content='if _ollama_embedding is None:'),
     Document(metadata={}, page_content='_ollama_embedding = OllamaEmbeddings('),
     Document(metadata={}, page_content='model=default_llm,'),
     Document(metadata={}, page_content='base_url=base_ollama_url, show_progress=True'),
     Document(metadata={}, page_content=')\n    return _ollama_embedding'),
     Document(metadata={}, page_content='set_langsmith_env()')]


