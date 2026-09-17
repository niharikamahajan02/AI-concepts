from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

from langchain_core.prompts import PromptTemplate
llm=HuggingFaceEndpoint(
  repo_id="deepseek-ai/DeepSeek-V3-0324"
)

model=ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact1',description='fact1 of topic'),
     ResponseSchema(name='fact2',description='fact2 of topic'),
      ResponseSchema(name='fact3',description='fact3 of topic')

]

parser=StructuredOutputParser.from_response_schemas(schema)
templ1=PromptTemplate(
    template="give 3 facts about {topic} \n {format_inst}", #prompt bante time additional instruction is given ki kis tarah ka ans chhaiye
    input_variables=['topic'],
    partial_variables={'format_inst':parser.get_format_instructions()} #befoire runtome , it fills,"" contract" the parser tells the LLM to follow, so that the same parser can later decode the LLM's output back into structured data



)

prompt=templ1.invoke({'topic':'black hole'})
res=model.invoke(prompt)

#chain=temp1 |model|parser
#res=chain.invoke({'topic':'black hole})
f_ans=parser.parse(res.content)
print(f_ans)

