import random
from abc import ABC, abstractmethod


class Runnable(ABC):
  @abstractmethod
  def invoke(input_data):
    pass 


#ab nakli llm bhi runnable bn gya to jb llm object banyegenge tb invoke krna hi padega
class NakliLLM(Runnable):
  def __init__(self):
    print('LLM created')

  def invoke(self, prompt):
    
   response_list = [
          'hi , how u came herer',
          'universe is very vast ',
          'tagda package milega :)'
      ]  
   return {'response': random.choice(response_list)}
   
  
#prdict nhi hatare coz it may be possible tha developerpurane use krre ho isse to bs notice that this function is going to be depreciated
  def predict(self, prompt):

    response_list = [
        'hi , how u came herer',
        'universe is very vast ',
        'tagda package milega :)'
    ]

    return {'response': random.choice(response_list)}

  #PROMPT
class NakliPromptTemplate:

    def __init__(self, template, input_variables):
      self.template = template
      self.input_variables = input_variables

    def invoke(self,input_dict):
      return self.template.format(**input_dict)
  
    def format(self, input_dict):
      return self.template.format(**input_dict)

templ=NakliPromptTemplate(
      template='wriet abht htid topic {topic}',
      input_variables=['topic']
    )

#prompt=templ.format({'topic':'india'})
#
#llm=NakliLLM()
#ans=llm.predict(prompt)
#print(ans)

#prompt template and llm componnt ko jodna




class NakliLLMChain:

  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt  

  def run(self, input_dict):

    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)

    return result['response']


class Runnableconnector(Runnable):

  def __init__(self, runnable_list):
    self.runnable_list=runnable_list

  def invoke(self,input_data):
    for listt in self.runnable_list:
      input_data=listt.invoke(input_data)

    return input_data
      
      
  

llm=NakliLLM()
template=NakliPromptTemplate(
  template='wriet abht{topic}',
  input_variables=['topic']
)

#chain=NakliLLMChain(llm,template)

chain=Runnableconnector([template,llm])

ans=chain.invoke({'topic':'indiaa'})
#ans=chain.run({'topic':'indiaa'})
print(ans)