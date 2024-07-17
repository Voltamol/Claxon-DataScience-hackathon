from fastapi import FastAPI,Body
from typing import List, Union
from pydantic import BaseModel
import pickle
import numpy as np
import os
app = FastAPI()

def preprocess(input_data):
    ...
    
class InputData(BaseModel):
    data: List[Union[float, int,str]]

app = FastAPI()

def getModel(modelName:str):
    current=os.getcwd()
    root=os.path.dirname(current)
    filename=f"{modelName}.pickle"
    path=os.path.join(root,current,filename)
    with open(path,"rb") as file:
        model=pickle.load(file)
    return model

def predict(modelName,array):
    model=getModel(modelName)
    preprocessed=preprocess(data)
    prediction = model.predict(preprocessed)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def items(item_id:int):
    return {"message": item_id}

@app.post("/models/rfc")
async def rfc_data(input_data:NumbersInput= Body(...)):
    data = input_data.data
    prediction=predict("rfc",data)
    return {"processed_numbers": prediction}
    
@app.post("/models/svc")
async def svc_data(input_data:NumbersInput= Body(...)):
    data = input_data.data
    prediction=predict("svc",data)
    return {"processed_numbers": prediction}
    
@app.post("/models/bnb")
async def bnb_data(input_data:NumbersInput= Body(...)):
    data = input_data.data
    prediction=predict("bnb",data)
    return {"processed_numbers": prediction}
    
@app.post("/models/xgb")
async def xgb_data(input_data:NumbersInput= Body(...)):
    data = input_data.data
    prediction=predict("xgb",data)
    return {"processed_numbers": prediction}
    
@app.post("/models/lr")
async def lr_data(input_data:NumbersInput= Body(...)):
    data = input_data.data
    prediction=predict("lr",data)
    return {"processed_numbers": prediction}