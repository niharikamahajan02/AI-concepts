#PRACTISE OF RETURNING THE RESPONSE IN A STRUCTURED ORDERR
#NO VALIDATION 

from typing import TypedDict,Annotated
class Person(TypedDict):
    name:str
    age:int

new_person: Person ={'name':'kruhf','age':23}

print(new_person)

# reviews->LLM-> {summary , sentiment} as dict

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
 repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

class review(TypedDict):
    summary:Annotated[str,"a brief summary of review"] #string vbhejan with kya description
    sentiment:str
    pros=Annotated[str,"wriet all pros inside list"]


structed_model=model.with_structured_output(review)

#During invikation a system promp also goes with the human msg as u r a ai aaistant that extracts insights from text ,
#  give poprdc review ssummary:brief oiobvverview, sentiment : tone of review . return res in jSON
res=structed_model.invoke("this is a parcel which is better than other parcels. Also its designed very elligently ,,Godd for dwaily uses")

print(res['summary'])
print(res['sentiment'])

