#FOR DATA VALIDATION ALSO
from dotenv import load_dotenv

load_dotenv()

#pip install pydantic

from pydantic import BaseModel 

class Student(BaseModel):
    name:str

new_str={'name':'nitish'}

student=Student(**new_str)
print(student)