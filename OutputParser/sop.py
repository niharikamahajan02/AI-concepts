from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
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

parser=StrOutputParser()

chain=templ1| model |parser | templ2 | model |parser

res=chain.invoke({'input1':'black hole'})
print(res)