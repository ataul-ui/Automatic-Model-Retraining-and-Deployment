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
        return "The result: machine will fail"
    elif the_answer[0] == want_test[0][1]:
        return "The result: machine will continue to work"
    else:
        return "There is an error somewhere in the code" 
    


if __name__ == "__main__":
    
    # for now I will keep streamlit comented out:
    
    
    st.title("Predictive Maintainance Form")
    st.write("This is a Streamlit app integrated with FastAPI.")

    
    device_type = st.radio("what is the device type?", ("M", "L", "H"))
    air_temp = st.selectbox("What is the air temp?", range(5, 501))
    process_temp = st.selectbox("What is the process temp?", range(5, 501))
    rot_speed = st.selectbox("What is the rot speed?", range(5, 501))
    torque = st.selectbox("What is the torque?", range(5, 501))
    tool_wear = st.selectbox("What is the tool wear?", range(5, 501))
    

    button_sub = st.button("submit")
    
    
    if button_sub:
        json_message = {
            #"Type": [device_type],
            "Air temperature [K]": [air_temp],
            "Process temperature [K]": [process_temp],
            "Rotational speed [rpm]": [rot_speed],
            "Torque [Nm]": [torque],
            "Tool wear [min]": [tool_wear]
        }
        

        send_to_predict = predict_failure(json_message)
        print(send_to_predict)
        st.write(send_to_predict)
        
        retrain_the_model = 0
        
    
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
