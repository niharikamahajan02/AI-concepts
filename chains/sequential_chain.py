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

p2=PromptTemplate(
    template='summarize {input2} in 5 lines',
    input_variables=['input2']
)
chain1=prompt | model | parser | p2 | model | parser 
ans=chain1.invoke({'input':'black hole'})




chain1.get_graph().print_ascii()

print(ans)