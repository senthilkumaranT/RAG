from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from llm import chat_completion


#embeddings
embeddings = OllamaEmbeddings(model="llama3.2")

#qdrant  url and api key
url = ""
api_key = ""


#qdrant vector store
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="",
    url=url,
    api_key=api_key,
)

#user question
question = "what is bitcoin?"

#similarity search
chunks = qdrant.similarity_search(query=question, k=1)

#prompt
prompt = f"""
context:{chunks[0].page_content}

Question:{question}


create a very short summary based on the provided context and user question.
give me the whole response in 3 lines
"""


#chat completion
chat_completion(prompt)