import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn
import json


class Model:
    def __init__(self, data):
        self.data = data
        #self.air_temp = air_temp
        # I'll create all the self instances later, once I figure out
        # if I should input the data this way or not
    
    #rename this to logistic_regression_model
    def trained_model(self):
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                self.data[column] = label_encoder.fit_transform(self.data[column])

        X = self.data.drop("Machine failure", axis=1)
        y = self.data["Machine failure"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(random_state=42, max_iter=10000, solver='saga')
        model.fit(X_train, y_train)

        return model


def result_return():
    
    
    data = pd.read_csv("machine_failure.csv")

    thing = Model(data)
    result = thing.trained_model()
    
    

    json_data = '''
    {
        "UDI": [50],
        "Product ID": ["L47438"],
        "Type": ["M"],
        "Air temperature [K]": [298.1],
        "Process temperature [K]": [309.1],
        "Rotational speed [rpm]": [1527],
        "Torque [Nm]": [28.6],
        "Tool wear [min]": [9],
        "TWF": ["0"],
        "HDF": ["2"],
        "PWF": ["0"],
        "OSF": ["0"],
        "RNF": ["0"]
    }
    '''

    
    # Parse the JSON data
    data = json.loads(json_data)
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Assuming you have a new data point stored in a DataFrame called 'new_data'
    label_encoder = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column])

    predictions = result.predict(df)
    want_test = pd.DataFrame([0,1])
    if predictions[0] == want_test[0].all():
        print("success")
    elif predictions[0] == want_test[1].all():
        print("whatever")
    else:
        print("what happened?")
    print(predictions[0])
    
    
    
    #want_test = pd.DataFrame([0,1])
    
    '''
    print(want_test)
    if want_test[0] == 0:
        print("success")
    elif want_test[1] == 0:
        print("fail")
    else :
        print("what?")
        
    '''

    return "off"


if __name__ == "__main__":
    result_return()
