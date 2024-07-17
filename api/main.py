from fastapi import FastAPI,Body
from typing import List, Union
from pydantic import BaseModel

app = FastAPI()

class NumbersInput(BaseModel):
    numbers: List[Union[float, int]]

app = FastAPI()

def getModel(modelName:str):
    path=""
    with open(path,"rb") as file:
        model=pickle.load(file)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def items(item_id:int):
    return {"message": item_id}

@app.post("/models/rfc")
async def rfc_data(data:NumbersInput= Body(...)):
    numbers = data.numbers
    prediction = 
    return {"processed_numbers": prediction}