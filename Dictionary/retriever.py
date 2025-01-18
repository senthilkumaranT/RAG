from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from sent import chat_completion



embeddings = OllamaEmbeddings(model="llama3.2")

url=""
api_key=""


qdrant =QdrantVectorStore.from_existing_collection(
    embedding=embeddings,   
    collection_name="",
    url=url,
    api_key=api_key,
)


question = input("enter your question ")


chunks =qdrant.similarity_search(query=question ,k=4)

prompt =f"""

content:{chunks}

Question :{question }

you are the best dictionary in the world , you will give me the correct meaning of the word user given and explain it in detail



"""





chat_completion(prompt)



