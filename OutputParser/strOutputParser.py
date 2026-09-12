from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

templ1=PromptTemplate(
    template="wriet me detailed explanation abot {input1}",
    input_variables=['input1']
)

templ2=PromptTemplate(
    template="wriet 5 sentence summary on  {txt}",
    input_variables=['txt']
)

prompt1=templ1.invoke({'input1':'black hole'})
res=model.invoke(prompt1)
prompt2=templ2.invoke({'txt':res.content})
res1=model.invoke(prompt2)

print(res1.content)