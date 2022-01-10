#Python
from typing import Optional,List,Dict
from enum import Enum
#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr,HttpUrl
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

class city(Enum):
    Bogota = 'bogota'
    Medellin = 'Medellin'
    Bucaramanga = 'bucaramanga'
    Barranquilla = 'barranquilla'

class Location(BaseModel):
    city: str = Field(..., min_length=1, max_length=50)
    state: str = Field(..., min_length=1, max_length=50)
    country: str = Field(..., min_length=1, max_length=50)

class Person(BaseModel):
    first_name: str = Field(...,min_length=1,max_length=50)
    last_name: str = Field(...,min_length=1,max_length=50)
    age: int = Field(...,gt=0,le=100)
    email: str = EmailStr(...)
    url: HttpUrl
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)
    password : str = Field(...,min_length=8)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "García Martoni",
    #             "age": 21,
    #             "hair_color": "blonde",
    #             "is_married": False
    #         }
    #     }  data for autoComplete

class PersonOut(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=100)
    email: str = EmailStr(...)
    url: HttpUrl
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)



class Net_info(BaseModel):
    email: str = EmailStr(...)
    url: HttpUrl


@app.get('/')
def home():
    return {'message': 'Hello World'}


#request and response

@app.post('/person/new',response_model=PersonOut)
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
            description='this is person name,its between 1 and 50 char',
            example="Rocío"
        ), #condiciones del QUERY
        age: int = Query(
            ...,
            gt=17,
            title='Person Age',
            description='this is the person age,its require',
            example=25
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
            description='This is the user Id,for all the user in ascend mode',
            example = 123
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

# @app.post('/person/{email}')
# def email(
#         email : str = Path(
#             ...,
#             title='Correo electronico',
#             description='email del usuario',
#             min_length=15,
#             max_length=50
#         ),
#         name: Optional[str] = Path(
#             default=None,
#             min_length=1,
#             max_length=50,
#             title='Person Name',
#             description='this is person name,its between 1 and 50 char'
#         )
#
# ):
#     return {'email':email}

# @app.post('/Net_info/new')
# def create_mail(net_info: Net_info = Body(...)):
#     return net_info


@app.post('/Net_info/{new}')
def email(
        new: str = Path(
            ...,
            title='Person ID',
            description='this is the person ID',

        ),
        net_info: Net_info = Body(...)

):
    result = net_info.dict()
    return result