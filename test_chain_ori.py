from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from common import get_llm, get_vector_store

model = get_llm()
vec = get_vector_store()

retriever = vec.as_retriever()

message = """
Answer this question using the provided context only.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | model

response = rag_chain.invoke("关于猫")
response
