from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_together import TogetherEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi #youtube library 
import os

## apikey for together
os.environ["TOGETHER_API_KEY"] = ""

#embeddings
embeddings = TogetherEmbeddings(model="togethercomputer/m2-bert-80M-8k-retrieval")

#video link for transcript
video_id = "GW7B6vwktPA"
transcript = YouTubeTranscriptApi.get_transcript(video_id)



# Convert transcript to text documents
documents = []
for entry in transcript:
    text = entry['text']
    documents.append({"text": text})



#  qdrant url and api key
url = ""  
api_key = ""

#vector store
qdrant = QdrantVectorStore.from_texts(
    texts=[doc["text"] for doc in documents],
    embedding=embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="videocaptions",
)