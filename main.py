#Python
from typing import Optional,List
from enum import Enum
#Pydantic
from pydantic import BaseModel
from pydantic import Field
#fastAPI
from fastapi import FastAPI # Import FastAPI.
from fastapi import Body,Query,Path

app = FastAPI() # Create an app instance.

#models

class HairColor(Enum):
    white = 'white'
    black = 'black'
    brown = 'brown'
    yellow = 'yellow'
    red = 'red'

class Location(BaseModel):
    city : str
    state : str
    country : str

class Person(BaseModel):
    first_name: str = Field(...,min_length=1,max_length=50)
    last_name: str = Field(...,min_length=1,max_length=50)
    age: int = Field(...,gt=0,le=100)
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)



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
        name: Optional[str] = Query(
            default=None,
            min_length=1,
            max_length=50,
            title='Person Name',
            description='this is person name,its between 1 and 50 char'
        ), #condiciones del QUERY
        age: int = Query(
            ...,
            gt=17,
            title='Person Age',
            description='this is the person age,its require'
        )
):
    return {name: age}

#Validaciones path parameters

@app.get('/person/detail/{person_id}')
def show_person (
        person_id:int = Path(
            ...,
            gt=0,
            title='Person Id',
            description='This is the user Id,for all the user in ascend mode'
        )
):
    return {person_id:'it exist'}

#Request Body

@app.put('/person/{person_id}')
def update_person(
        person_id: int = Path(
            ...,
            title='Person ID',
            description='this is the person ID',
            gt=0
        ),
        person: Person = Body(...),
        location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results

#Request Body validarions

#Se hace en la definicion del modelo arriba