from fastapi import FastAPI # Import FastAPI.
from enum import Enum
from pydantic import BaseModel

app = FastAPI() # Create an app instance.

@app.get('/') # Write a path operation decorator (like @app.get("/")).
def home():
    return {'message': 'Hello World'} # Write a path operation function (like def root(): ... above).

# Run the development server (like uvicorn main:app --reload).


#Path Parameters

#The value of the path parameter item_id will be passed to your function as the argument item_id.
@app.get("/items/{item_id}")
async def read_item(item_id): #*Path Parameters
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: int): # Path parameters with types
    return {"item_id": item_id}

#----------------------------------*****************************--------------------------------------

#Order matters

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"},\
           {'user_id': 'luisa is the user'},\
    [{"user_id": "the current user"},
           {'user_id': 'luisa is the user'},]


@app.get("/users/{user_id}")
async def read_user(user_id: str): #*Path Parameters
    return {"user_id": user_id}


#Create MODEL

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#REQUEST BODY

# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A request body is data sent by the client to your API. A response body is the data your API sends to the client.

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

