from fastapi import FastAPI # Import FastAPI.
from enum import Enum

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

