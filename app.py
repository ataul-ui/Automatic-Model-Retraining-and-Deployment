from fastapi import FastAPI
import uvicorn
from ml_code import test_predictive_maintaincence
from testing import result_return
import requests

'''

response = requests.post('/url/to/query/')
# Assert that the response is successful (status code 200)
assert response.status_code == 200
'''


app = FastAPI()

@app.get("/")
def root():
    return {"message": "something"}

@app.get("/v1/pred")
async def users():
    accuracy = test_predictive_maintaincence()
    return {"message": accuracy}

@app.post("/v1/pred")
async def prediction():
    return {"answer": "failure or not"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
