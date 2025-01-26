from qdrant_client import QdrantClient# qdrant client
from docling.chunking import HybridChunker# chunking
from docling.datamodel.base_models import InputFormat# doc converter
from docling.document_converter import DocumentConverter# doc converter
from llm import * # llm
import streamlit as st 



# set url and api key
url = ""  
api_key = ""



# qdrant client
client = QdrantClient(url=url,api_key=api_key)

# set model
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")


def retrieve(collection_name ,question):
    # query
    points = client.query(
    collection_name=collection_name,
    query_text=question,
    limit=5,
    )



    # final response
    final_response =" "


    # loop through points
    for i, point in enumerate(points):
        final_response += point.document

   
    
    

    #prompt
    prompt =f"""
    context :{final_response}

    Quesiton :{question}



    You are a recipe maker. The user will provide a list of available vegetables, and you will suggest dishes with their dish name that can be prepared using them.
    first list the dishes name
    list the producer of the recipe in step1 step2 order 

    if any item did not match for the dish  you have  to tell that there is no match receipe 


    """



    


    
    llm_answer = chat_completion(prompt,"openai/gpt-4o-mini")

    return llm_answer

print(retrieve("indian-receipe","availabe item : beans , carrot , cabage, cauliflower ,rice "))



