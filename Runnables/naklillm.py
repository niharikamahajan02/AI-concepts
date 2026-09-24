import random

class NakliLLM:
  def __init__(self):
    print('LLM created')

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
  
    def format(self, input_dict):
      return self.template.format(**input_dict)

templ=NakliPromptTemplate(
      template='wriet abht htid topic {topic}',
      input_variables=['topic']
    )

prompt=templ.format({'topic':'india'})

llm=NakliLLM()
ans=llm.predict(prompt)
print(ans)