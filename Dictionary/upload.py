from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorstore 
from langchain_ollama import OllamaEmbeddings
from llm import chat_completion

embeddings =OllamaEmbeddings(model="llama3.2")


loader = PyPDFLoader("largedictionary.pdf")
pages =loader.load_and_split()


url=""
api_key=""


qdrant = QdrantVectorStore.from_documents(
    pages,
    embeddings,
    url=url,
    api_key=api_key,
    collection_name="",

)


