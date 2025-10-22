from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = 'Faraz'
    age : Optional[int] = None
    email : EmailStr
    CGPA : float = Field(gt=0, lt=10, default=5, description='A decimal value representing the CGPA of the student')

new_student = {'name' : 'Faraz',
               'age' : '32',
               'email' : 'abc@gamil.com',
               'CGPA': 5}

student = Student(**new_student)

print(type(student))
print(student)