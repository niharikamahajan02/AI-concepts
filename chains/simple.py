from langchain_huggingface  import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='tell me about {input}',
    input_variables=['input']
)
parser=StrOutputParser()

chain=prompt | model | parser

chain.get_graph().print_ascii()

res=chain.invoke({
    'input':'black hole'
})

print(res)