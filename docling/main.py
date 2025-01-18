from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter




# ## url and api key qdrant 
url = "" ## use your url
api_key ="" ## use your api key



# doc converter
doc_converter = DocumentConverter(allowed_formats=[InputFormat.HTML])
client = QdrantClient(url=url,api_key=api_key)


# set model
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")


# convert doc

result = doc_converter.convert(
    "https://www.sagacify.com/news/a-guide-to-chunking-strategies-for-retrieval-augmented-generation-rag"
)




# chunking
documents, metadatas = [], []
for chunk in HybridChunker().chunk(result.document):
    documents.append(chunk.text)
    metadatas.append(chunk.meta.export_json_dict())



# add to qdrant
qdrant = client.add(
    collection_name="docling",
    documents=documents,
    metadata=metadatas,
    batch_size=64,
)