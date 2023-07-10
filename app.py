from fastapi import FastAPI
import uvicorn
from ml_code import test_predictive_maintaincence

app = FastAPI()

@app.get("/")
def root():
    accuracy = test_predictive_maintaincence()
    return {"message": accuracy}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
