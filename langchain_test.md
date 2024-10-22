```python

import os

lang_smith_api_key = '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'

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = lang_smith_api_key

```


```python
from langchain_community.llms.ollama import Ollama

ollama = Ollama(model="qwen2.5:14b",base_url="http://gpt:11434")

print(ollama("你是谁"))

```

    你好！有什么可以帮助你的吗？
    
