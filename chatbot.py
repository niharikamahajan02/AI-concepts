from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage, SystemMessage
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324"
)
chat_history=[
    SystemMessage(content="u r helpul assistant")

]

model=ChatHuggingFace(llm=llm)

while True:
    user_inp=input("you:")
    if(user_inp=="exit"): break
   
    chat_history.append( HumanMessage(content=user_inp))
    res=model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    print("Ai",res.content)



print(chat_history)