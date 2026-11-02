from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()
llm=HuggingFaceEndpoint(
  repo_id="openai/gpt-oss-120b"
)
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

#indexing
video="DsewHeVbL-0"

try:
    ytt_api = YouTubeTranscriptApi()

    transcript = ytt_api.fetch(video, languages=["en"])

    transcript_list = transcript.to_raw_data()
    
    ts=" ".join(chunk["text"] for chunk in transcript_list)
    print(ts)

except TranscriptsDisabled:
    print("no captions ")

#chunking
splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks=splitter.create_documents([ts]) #doc list
#print(chunks[0])

#embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)
vector_store = Chroma(
    embedding_function=embeddings,
    persist_directory='my_chroma_db2',
    collection_name='sample'
)
print(vector_store)
vector_store.add_documents(chunks)
#retriiver
retriever = vector_store.as_retriever(
    search_type="similarity",                   # <-- This enables MMR
    search_kwargs={"k": 2} # k = top results, lambda_mult = relevance-diversity balance 0->exact ismilar , 1->show diversity
)
ans=retriever.invoke("whats deep mind")
print(ans)