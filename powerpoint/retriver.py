from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from sent import chat_completion
from langchain_ollama import OllamaEmbeddings
import streamlit as st

#embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#qdrant  url and api key
url = ""
api_key = ""


qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="powerpoint",
    url=url,
    api_key=api_key,
)


st.title("RAG using powerpoint ")

## user question 
question = st.text_input("Enter your question")


#similarity search 
chunks = qdrant.similarity_search(query=question, k=2)

#prompt
prompt =f"""

content :{chunks[0].page_content}

Question :{question}

Please provide a concise 3-line summary of the content that directly answers the question.
Make sure to write complete sentences and avoid breaking up words.
Keep the response clear and coherent.

"""


st.write(chat_completion(prompt))



