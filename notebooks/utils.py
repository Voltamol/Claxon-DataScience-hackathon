import pickle
import os
import numpy as np
current=os.path.dirname(__file__)
source=os.path.join(current,'pickle')

expected=['gender', 'currency', 'is_employed', 'job', 'location', 'loan_amount',
       'number_of_defaults', 'outstanding_balance', 'interest_rate', 'age',
       'remaining term', 'salary', 'marital_status']

def get_path(filename):
    return os.path.join(source,filename)

pickle_files=[
    "bnb.pickle",
    "encoders.pickle",
    "gnb.pickle",
    "lr.pickle",
    "rfc.pickle",
    "scaler.pickle",
    "svc.pickle"

]

def read_pickle(filename):
    with open(filename,'rb') as iowrapper:
        obj=pickle.load(iowrapper)
    return obj

def get_pickle():
    pickle={}
    for filename in pickle_files:
        path=get_path(filename)
        obj=read_pickle(path)
        obj_name=filename.split('.')[0]
        pickle[obj_name]=obj
    return pickle

def preprocess(arr,scaler,encoders,):
    for key in encoders:
        if isinstance(key,int):
            encoder=encoders[key]
            arr[key]=encoder.transform([arr[key]])[0]
    scaled=scaler.transform([arr])
    return scaled

def predict(data,model,target_encoder):
    prediction=model.predict(data)
    label=target_encoder.inverse_transform(prediction)
    return label[0]