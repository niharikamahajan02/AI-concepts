from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324"
)
chat_history=[]

model=ChatHuggingFace(llm=llm)

while True:
    user_inp=input("you:")
    chat_history.append(user_inp)
    res=model.invoke(chat_history)
    chat_history.append(res.content)
    print("Ai",res.content)



print(chat_history)