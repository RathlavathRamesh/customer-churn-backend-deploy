import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler, LabelEncoder
from fastapi import FastAPI
from pydantic import BaseModel
import pickle 


app=FastAPI()


class ChustomerFeatures(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    
geograpy_map={'France': 0, 'Spain': 1, 'Germany': 2}
gender_map={'Female': 0,'Male': 1}

@app.post('/predict')
def predict_churn(features: ChustomerFeatures):
    df = features.dict()
    df['Geography'] = geograpy_map.get(df['Geography'], 0)
    
    df['Gender'] = gender_map.get(df['Gender'], 0)
    scaler = pickle.load(open('./scaler.pkl','rb'))
    X=pd.DataFrame([df])
    X_scaled = scaler.transform(X)
    model = load_model('./bank_churn_model.h5')
    prediction = model.predict(X_scaled)[0][0]
    
    return {f'Churn Probability {float(prediction)} churned': int(prediction> 0.5)}