#user feedback ->model ->extract + or - sentiment a -> acc thanks or sorry for inconv
from langchain_huggingface  import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel ,Field
from typing import Literal
from langchain_core.runnables import RunnableBranch,RunnableLambda
load_dotenv()

from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)





class feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='give sentiment of feedback')

parser2=PydanticOutputParser(pydantic_object=feedback)

parser=StrOutputParser()
prompt=PromptTemplate(
    template='tell me sentiment of user answer {input} in positive or negative {format_instruction}',
    input_variables=['input'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)
chain1 =prompt | model |parser2 #classify review

#ans=chain1.invoke({'input':'Its a very bad device'}).sentiment
#
#print(ans)

promptpos=PromptTemplate(
    template='tell me somthing for this positive review {input}',
    input_variables=['input']
)

promptneg=PromptTemplate(
    template='tell me somthing for this negative review {input}',
    input_variables=['input']
)

branchchain=RunnableBranch(
    (lambda x: x.sentiment=='positive' , promptpos |model |parser),
    #(conditoin1, branch),
    (lambda x: x.sentiment=='negative' , promptneg |model |parser),
    #converting default lambda function to runnable lambde to convert it into chain
  RunnableLambda( lambda x:"could not find sentiment")
)

final_chain=chain1 | branchchain
print(final_chain.invoke({'input':'its beautiful phone'}))
