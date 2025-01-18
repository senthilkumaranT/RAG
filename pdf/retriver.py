from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from sent import chat_completion
from langchain_ollama import OllamaEmbeddings

#embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#qdrant  url and api key
url = ""
api_key = ""


qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="11067791.pdf",
    url=url,
    api_key=api_key,
)


## user question 
question ="what is the title of the pdf "


#similarity search 
chunks = qdrant.similarity_search(query=question, k=1)

#prompt
prompt =f"""

content :{chunks[0].page_content}

Question :{question}

create a very short summary based on the provided context and  user question .
give me the whole  response in 3 line



"""


chat_completion(prompt)



