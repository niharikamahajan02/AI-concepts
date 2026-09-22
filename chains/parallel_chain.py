from langchain_huggingface  import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core import runnables

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

#ek mdel notes generate jrega and 1 model quiz parallely 
# then dono model ke ans merge honge to create ques ans

parallel_chain=runnables({
    'notes_ch':pr1 |model| parser,
    'quiz':pr2 | model | parser
})

merge= p3 | model| StrOutputParser

chain=parallel_chain | merge

text="""jefvbljrghfldhjfgluhds"""

chain.invoke('text':text  )