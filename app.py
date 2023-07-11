from fastapi import FastAPI
import uvicorn
#from ml_code import test_predictive_maintaincence
from testing import result_return
import pandas as pd
import requests
import json

'''

response = requests.post('/url/to/query/')
# Assert that the response is successful (status code 200)
assert response.status_code == 200
'''


app = FastAPI()

def preprocess_data(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    return df

@app.get("/")
def root():
    return {"message": "something"}


@app.post("/predict")
def predict_failure(data: dict):
    df = preprocess_data(data)
    the_answer = result_return(df)
    
    want_test = pd.DataFrame([0,1])
    if the_answer[0] == want_test[0].all():
        return {"message": "success"}
    elif the_answer[0] == want_test[1].all():
        return {"message": "whatever"}
    else:
        return {"message": "whatever"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
