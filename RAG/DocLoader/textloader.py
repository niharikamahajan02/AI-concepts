from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm=HuggingFaceEndpoint(
  repo_id="openai/gpt-oss-120b"
)
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)
prompt=PromptTemplate(
    template="wriet summary of foll topic {poem}",
    input_variables=['poem']
)

parser=StrOutputParser()



file_path = Path(__file__).parent / "cric.txt"

loader = TextLoader(str(file_path), encoding="utf-8")
docs = loader.load()

chain=prompt | model |parser

ans=chain.invoke({'poem':docs[0].page_content})
print(ans)

print(type(docs))
print(docs[0].page_content)