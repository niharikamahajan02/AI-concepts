from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

llm=HuggingFaceEndpoint(
     repo_id="deepseek-ai/DeepSeek-V3-0324"
    
)


model=ChatHuggingFace(llm=llm)
msg=[
    SystemMessage(content="you r a ai assistant "),
    HumanMessage(content="what capoital of india")

]


res=model.invoke(msg)
msg.append(AIMessage(res.content))
print(msg)