from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from testing import result_return
from pydantic import BaseModel
import pandas as pd
import streamlit as st
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

#rename the path to /logistic_model   instead of /predict
@app.post("/predict")
def predict_failure(data: dict):
    #oh wow this works
    #json_compatible_item_data = jsonable_encoder(item)
    #the json encoder can convert it back into json message
    #return data
    json_data = json.dumps(data)
    #json_compatible_item_data = jsonable_encoder(data)
    #return json_compatible_item_data
    
    the_answer = result_return(json_data)
    want_test = pd.DataFrame([0,1])
    if the_answer[0] == want_test[0].all():
        return "success"
    elif the_answer[0] == want_test[1].all():
        return "whatever"
    else:
        return "what happened?"'''
    
    df = preprocess_data(data)
    the_answer = result_return(df)
    
    want_test = pd.DataFrame([0,1])
    if the_answer[0] == want_test[0].all():
        return {"message": "success"}
    elif the_answer[0] == want_test[1].all():
        return {"message": "whatever"}
    else:
        return {"message": "whatever"}
        '''


if __name__ == "__main__":
    st.title("My Streamlit App")
    st.write("This is a Streamlit app integrated with FastAPI.")
    # I can pass in the json message through here,
    # st as the front end will give the message,
    # then st will print the result given by the model (success) in the front end
    # so the story is that a technician is measuring the machine and he
    # is inputing choices from the drop down menu
    # each new choice will be under a new header giving explaination
    
    temp = st.radio("what is the device type?", ("M", "L", "H"))
    button_sub = st.button("submit")
    
    
    
    # the if button will be on the last step
    if button_sub:
        print(temp)
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
