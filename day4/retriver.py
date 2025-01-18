
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from llm import token 
import streamlit as st 
embeddings = OllamaEmbeddings(model="llama3.2")


url = ""  
api_key = ""
 


qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="braintumour",
    url=url,
    api_key=api_key,
)


st.title("rag using brain tumour")

url =st.text_input("enter the url of image")


question =st.text_input("enter your question ")

chunks =qdrant.similarity_search(question ,k=5)


prompt =f"""

context :{chunks}

Question: {question}

Check it the given image is brain tumor or not. If not tell "I dont know" and do not answer the question.
Else Answer the question based on the image.
"""


if st.button("Get Answer"):
    print(prompt)
    ret =token(question, "x-ai/grok-2-vision-1212", url)
    print(ret)
    st.write(ret)
