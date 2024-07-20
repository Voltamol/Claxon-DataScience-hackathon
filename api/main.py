from fastapi import FastAPI,Body
from typing import List, Union
from pydantic import BaseModel
from utils import expected
from utils import get_pickle
from utils import preprocess
from utils import predict
app = FastAPI()

objs=get_pickle()
scaler=objs['scaler']
encoders=objs['encoders']
bnb=objs['bnb']
gnb=objs['gnb']
svc=objs['svc']
rfc=objs['rfc']
lr=objs['lr']
target_encoder=encoders['target']

class NumbersInput(BaseModel):
    data: List[Union[float, int,str]]

app = FastAPI()


@app.get("/ExampleData")
async def Example():
    return {"sample": ['female', 'USD', True, 'Teacher', 'Beitbridge', 39000.0, 0,48653.01147325887, 0.22, 37, '47', 3230.038868649578, 'married']}

@app.post("/models/rfc")
async def rfc_data(sample:NumbersInput= Body(...)):
    scaled=preprocess(sample,scaler,encoders)
    prediction=predict(scaled,rfc,target_encoder)
    return {"processed_numbers": prediction}
    
@app.post("/models/svc")
async def svc_data(sample:NumbersInput= Body(...)):
    scaled=preprocess(sample,scaler,encoders)
    prediction=predict(scaled,rfc,target_encoder)
    return {"processed_numbers": prediction}
    
@app.post("/models/bnb")
async def bnb_data(sample:NumbersInput= Body(...)):
    scaled=preprocess(sample,scaler,encoders)
    prediction=predict(scaled,bnb,target_encoder)
    return {"processed_numbers": prediction}
    
@app.post("/models/gnb")
async def xgb_data(sample:NumbersInput= Body(...)):
    scaled=preprocess(sample,scaler,encoders)
    prediction=predict(scaled,gnb,target_encoder)
    return {"processed_numbers": prediction}
    
    
@app.post("/models/lr")
async def lr_data(sample:NumbersInput= Body(...)):
    scaled=preprocess(sample,scaler,encoders)
    prediction=predict(scaled,lr,target_encoder)
    return {"processed_numbers": prediction}