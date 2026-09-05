from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage, SystemMessage
from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V3-0324"
)
chat_history=[
   
    
]
#chat template
chat_temp=ChatPromptTemplate([
     ('system','your ai assistant of domain customer care'),

      MessagesPlaceholder(variable_name='chat_history'),
      ('human','{query}')
])


#load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())


prompt=chat_temp.invoke({'chat_history':chat_history, 'query':'where is my oorder'})
#prompt=chat_temp.invoke([
#    'domain':'AI',
#    'id':'iwurfh'
#])
model=ChatHuggingFace(llm=llm)


res=model.invoke(prompt)
print(prompt)



print(chat_history)