from langchain_community.document_loaders import TextLoader
from pathlib import Path

file_path = Path(__file__).parent / "cric.txt"

loader = TextLoader(str(file_path), encoding="utf-8")
docs = loader.load()

print(type(docs))
print(docs[0].page_content)