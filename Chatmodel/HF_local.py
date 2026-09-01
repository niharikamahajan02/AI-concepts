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

res=model.invoke("capital of india")

print(res.content)