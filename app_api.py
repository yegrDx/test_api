from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel
import sklearn

app = FastAPI()

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

request_count = 0

class PredictionInput(BaseModel):
    Pclass: int
    Age: float
    Fare: float
    
@app.get('/stats')
def stats():
    return {'return_count': request_count}

@app.get('/health')
def health():
    return {'status': "Ok"}

@app.post('/predict_model')
def predict_model(input_data: PredictionInput):
    global request_count
    request_count += 1

    new_data = pd.DataFrame({
        'Pclass': [input_data.Pclass],
        'Age': [input_data.Age],
        'Fare': [input_data.Fare]

    })

    predictions = model.predict(new_data)

    result = 'Survived' if predictions[0] == 1 else "Not Survived"
    return {'prediction': result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)