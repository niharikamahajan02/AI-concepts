from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

doc = [
    "virat is good",
    "sachin knows",
    "hello don"
]

query = "virat"

doc_emb = embedding.embed_documents(doc)
query_emb = embedding.embed_query(query)

res = cosine_similarity([query_emb], doc_emb)[0]
an=sorted(list(enumerate(res)), key=lambda x: x[1])
print(an)