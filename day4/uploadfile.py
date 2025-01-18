from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings  


#embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#load the document
loader = PyPDFLoader("braintumour.pdf")
pages = loader.load_and_split() 



#url and api key
url = ""  
api_key = ""


#vector store
qdrant = QdrantVectorStore.from_documents(
    pages,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="braintumour",
)
print(pages)