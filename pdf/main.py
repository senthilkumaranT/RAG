from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

###embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#loader
loader = PyPDFLoader("11067791.pdf")
pages = loader.load_and_split()



## url and api key 

url=""
api_key=""




###qdrant vector store
qdrant = QdrantVectorStore.from_documents(
    pages,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="11067791.pdf",
)