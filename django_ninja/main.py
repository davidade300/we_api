from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# Path parameter operation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Query parameter operation
@app.get("/items/")