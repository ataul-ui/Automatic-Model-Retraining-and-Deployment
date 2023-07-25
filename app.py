from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from ml_model import result_return
from pydantic import BaseModel
import pandas as pd
import streamlit as st
import requests
import json

app = FastAPI()

def preprocess_data(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    return df

@app.get("/")
def root(data: dict):
    return data

#rename the path to /logistic_model   instead of /predict
@app.post("/predict")
def predict_failure(data: dict):

    
    json_data = json.dumps(data)

    
    the_answer = result_return(json_data)
    senting = the_answer[0]
    #json_compatible_item_data = jsonable_encoder(senting)
    print(senting)
    
    
    want_test = pd.DataFrame([0,1])
    if the_answer[0] == want_test[0][0]:
        return "machine will fail"
    elif the_answer[0] == want_test[0][1]:
        return "machine will continue to work"
    else:
        return "There is an error somewhere in the code" 
    


if __name__ == "__main__":
    
    # for now I will keep streamlit comented out:
    
    
    st.title("Predictive Maintainance Form")
    st.write("This is a Streamlit app integrated with FastAPI.")
    # I can pass in the json message through here,
    # st as the front end will give the message,
    # then st will print the result given by the model (success) in the front end
    # so the story is that a technician is measuring the machine and he
    # is inputing choices from the drop down menu
    # each new choice will be under a new header giving explaination
    
    device_type = st.radio("what is the device type?", ("M", "L", "H"))
    air_temp = st.selectbox("What is the air temp?", range(5, 501))
    process_temp = st.selectbox("What is the process temp?", range(5, 501))
    rot_speed = st.selectbox("What is the rot speed?", range(5, 501))
    torque = st.selectbox("What is the torque?", range(5, 501))
    tool_wear = st.selectbox("What is the tool wear?", range(5, 501))
    
    #another question could be a st.radio:
    #What model do you want to test this on, that option could be sent to 
    #the testing.py, 
    #actually the model training stuff will only be done in testing.py model class,
    # but the model being called will only pass through def model_version()
    button_sub = st.button("submit")
    
    
    # the if button will be on the last step
    if button_sub:
        json_message = {
            #"Type": [device_type],
            "Air temperature [K]": [air_temp],
            "Process temperature [K]": [process_temp],
            "Rotational speed [rpm]": [rot_speed],
            "Torque [Nm]": [torque],
            "Tool wear [min]": [tool_wear]
        }
        
        #send_to_root = root(json_message)
        send_to_predict = predict_failure(json_message)
        print(send_to_predict)
        #print(device_type)
        st.write(send_to_predict)
        
        retrain_the_model = 0
        
    
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
