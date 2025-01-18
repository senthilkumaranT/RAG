from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings

#embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#loader
loader = PyPDFLoader("bitcoin.pdf")
pages = loader.load_and_split()

#qdrant url and api key

url = ""
api_key = ""

#qdrant vector store
qdrant = QdrantVectorStore.from_documents(
    pages,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="bitcoin",
)
