from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import UnstructuredPowerPointLoader

###embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#loader
loader = UnstructuredPowerPointLoader("Copy of Cute Blackboard Student Council Presentation (1).pptx")
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
    collection_name="powerpoint",
)