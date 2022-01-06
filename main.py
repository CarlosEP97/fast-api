#Python
from typing import Optional,List
#Pydantic
from pydantic import BaseModel
#fastAPI
from fastapi import FastAPI # Import FastAPI.
from fastapi import Body,Query

app = FastAPI() # Create an app instance.

#models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None



@app.get('/')
def home():
    return {'message': 'Hello World'}


#request and response

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query Parameters

@app.get('/person/detail')
def show_person(
        name: Optional[str] = Query(None, min_length=1, max_length=50),
        age: str = Query(...)
):
    return {name: age}
