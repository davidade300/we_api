from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# Path parameter operation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Path parameter operation
# those are evaluated in order, so if you have a fixed path that returns information
# about the current user or something like that, you need to make sure that the path
# for the fixed operation is declared before the dynamic path operation otherwise, the
# dynamic path would also match the fixed path "thinking" that it's receiving a parameter
# with the fixed value as its value.
@app.get("/users")
async def read_users():
    return ["Bean", "Elfo"]


# If you have a path operation that receives a path parameter,
# but you want the possible valid path parameter values to be predefined,
# you can use a standard Python Enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "DeepLearning for the win"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
