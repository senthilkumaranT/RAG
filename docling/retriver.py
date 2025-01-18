from qdrant_client import QdrantClient# qdrant client
from docling.chunking import HybridChunker# chunking
from docling.datamodel.base_models import InputFormat# doc converter
from docling.document_converter import DocumentConverter# doc converter
from llm import *# llm


# set collection name
COLLECTION_NAME = "docling"

# set url and api key
url = ""
api_key ="" 


# qdrant client
client = QdrantClient(url=url,api_key=api_key)

# set model
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")


# set question
question ="what are the documents formate are in  document specific chunking "


# query
points = client.query(
    collection_name=COLLECTION_NAME,
    query_text=question,
    limit=2,
)



# final response
final_response = " "


# loop through points
for i, point in enumerate(points):
    final_response += point.document




#prompt
prompt =f"""
context :{final_response}

Quesiton :{question}


you are a document expert and you can answer the question based on the document only give the answer based on given context




"""


print(prompt)




print(chat_completion(prompt,"meta-llama/llama-3.2-90b-vision-instruct:free"))





