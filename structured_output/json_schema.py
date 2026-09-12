#FOR DATA VALIDATION ALSO
from dotenv import load_dotenv

load_dotenv()

#pip install pydantic

from pydantic import BaseModel ,Field 

class Student(BaseModel):
    name:str

new_str={'name':'nitish'}

student=Student(**new_str)
s_dict=dict(student)

print(s_dict['name'])
print(student)



from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from typing import Optional,Literal

load_dotenv()

llm=HuggingFaceEndpoint(
 repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

#json schema used here 

structed_model=model.with_structured_output(review)

#During invikation a system promp also goes with the human msg as u r a ai aaistant that extracts insights from text ,
#  give poprdc review ssummary:brief oiobvverview, sentiment : tone of review . return res in jSON
res=structed_model.invoke("this is a parcel which is better than other parcels. Also its designed very elligently ,,Godd for dwaily uses")

print(res.summary)
print(res.sentiment)

