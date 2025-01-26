# Import necessary libraries for Qdrant client, document processing, and text splitting
from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from langchain_text_splitters import CharacterTextSplitter

# Set up Qdrant client with URL and API key
url = ""  
api_key = ""
client = QdrantClient(url=url, api_key=api_key)

# Configure the models for the Qdrant client
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")

# Function to upload a PDF document to a specified Qdrant collection
def upload_pdf(file_path, collection_name):
    # Initialize document converter with supported formats
    doc_converter = DocumentConverter(
        allowed_formats=[
            InputFormat.PPTX,
            InputFormat.PDF,
            InputFormat.DOCX,
            InputFormat.XLSX,
        ]
    )

    # Convert the document from the specified file path
    document = doc_converter.convert(file_path)

    # Prepare to process document chunks
    documents, metadatas = [], []
    text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=0)
    chunks = text_splitter.split_text(document.text)

    # Loop through each chunk and store it along with its metadata
    for chunk in chunks:
        documents.append(chunk)
        metadatas.append(document.meta.export_json_dict())

    # Upload the processed documents to the specified Qdrant collection
    qdrant = client.add(
        collection_name=collection_name,
        documents=documents,
        metadata=metadatas,
        batch_size=64
    )

# Call the upload_pdf function with the specified PDF file and collection name
upload_pdf("Indian-Recipes.pdf", "indian-receipe")