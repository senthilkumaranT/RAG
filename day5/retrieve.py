from langchain_qdrant import QdrantVectorStore
from langchain_together import TogetherEmbeddings
import streamlit as st 
import os 
from llm import token 




## together api key 
os.environ["TOGETHER_API_KEY"] = ""



## embeddings 
embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval")




## qdrant url and api key 
url = ""  
api_key = ""


## vector retrieval 
qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="videocaptions",
    url=url,
    api_key=api_key,
)



##user question 
question = st.text_input("enter your question :")


## similarity search with error handling

chunks = qdrant.similarity_search(question, k=10)



# chunks = []
# if question:  # Only search if there's a question
#     try:
#         chunks = qdrant.similarity_search(question, k=10)
#     except Exception as e:
#         st.error("Error retrieving similar chunks. Please try again.")
#         print(f"Error: {str(e)}")



## prompt 
prompt = f"""

context:{chunks}

Question :{question}


based on the user question about the video and answer the question based on the context 


"""

    ### finale response 
if st.button("get answer"):
    if chunks:  # Only proceed if we have chunks
        print(prompt)
        try:
            response = token(prompt, "mistralai/mixtral-8x7b-instruct")  # Removed :nitro suffix
            st.write(response)
        except Exception as e:
            st.error(f"Error getting response: {str(e)}")
    else:
        st.warning("Please enter a valid question first")
