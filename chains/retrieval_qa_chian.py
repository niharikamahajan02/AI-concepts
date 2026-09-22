from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(
    model_id="deepseek-ai/DeepSeek-V3-0324",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )

)

model=ChatHuggingFace(llm=llm)

#doc splitter
#embded
#store in faiss
vecotrestore=FAISS.from_documents(docs, embeddinggs())

retriver=vectorestore.as_retriever()

#qa retru chain
qa_chain=RetrievalQA.from_chain_type(llm=llm, retriver=retriever)
query="whats key takeaways"

ans=qa_chain.run(query)

