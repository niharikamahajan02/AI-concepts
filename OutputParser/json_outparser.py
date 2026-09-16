from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

templ1=PromptTemplate(
    template="give me name , age of fictional person {format_inst}", #prompt bante time additional instruction is given ki kis tarah ka ans chhaiye
    input_variables=[],
    partial_variables={'format_inst':parser.get_format_instructions()} #befoire runtome , it fills


)

#prompt=templ1.format()
#res=model.invoke(prompt)


#print(prompt)
#f_ans=parser.parse(res.content)
chain=templ1 | model |parser 
res=chain.invoke({})
#print(res.content)

print(res)
#print(f_ans)