from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from llm import chat_completion 
import streamlit as st
# embeddings 
embeddings=OllamaEmbeddings(model="llama3.2")


### url and api
url = ""
api=""



model = "x-ai/grok-2-1212"



### 
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="dictionary",### from upload get name 
    url=url,
    api_key=api,

)


## question 
question = st.text_input("enter the any question about student details ")




## similarity search 
chunks = qdrant.similarity_search(query=question, k=5)


#prompt
prompt =f"""

content :{chunks}

Question :{question}

give a detail about the student which the user given name 


"""


print(prompt)



st.write(chat_completion(prompt,model))


