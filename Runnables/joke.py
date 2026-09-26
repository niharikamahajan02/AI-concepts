from langchain_huggingface  import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core import runnables
from langchain_core.runnables import RunnableSequence

load_dotenv()

from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='tell me any joke about {input}',
    input_variables=['input']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)

cha=prompt | model |parser


print(cha.invoke({'input':'fish'}))