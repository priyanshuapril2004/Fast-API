import uvicorn 
from fastapi import FastAPI
from input import getData, heartInput
# import joblib

app =FastAPI()
# model= joblib.load('model.pkl')    
# get, post, update, delete 
@app.get('/')
def index():
    return {'message':'Hello Students, How are you!!'}

@app.get('/name')
def printNaam():
    return {'message':'Hello Karanpreet'}

# @app.get('/{name}')
# def getName(name:str):
#     return {'Name is':f'{name}'}
# @app.post('/{name}')
# def getName(name:str):
#     return {'Name is':f'{name}'}

@app.post('/getname')
def getName(data:getData):
    dict_data= data.model_dump() #Export the model instance to a dictionary
    print(dict_data)
    
    return dict_data

@app.post('/heartdisease')
def heartDis(data: heartInput):
    data= data.model_dump()
    age=data['age']
    sex=data['sex']
    cp= data['cp']
    trestbps= data['trestbps'] 
    chol= data['chol']
    fbs = data['fbs']
    restecg= data['restecg']
    thalach= data['thalach']
    exang= data['exang']
    oldpeak=data['oldpeak']
    slope= data['slope']
    ca= data['ca']
    thal= data['thal']
    
    host_data= [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    pred_result = model.predict([host_data])
    
    if pred_result[0]==1:
        prediction= "Heart Disease Detected"
    else:
        prediction="No Heart Disease"
        
    return prediction


# to run fastapi - uvicorn filename:objectname --reload

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
    
    