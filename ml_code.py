import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn



class Model:
    def __init__(self, data): #, air_temp ,process_temp, rot_speed, torque, tool_wear):
        self.data = data
        #self.air_temp = air_temp
        # I'll create all the self instances later, once I figure out
        # if I should input the data this way or not
        return 
    
    def trained_model(self):
        
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                self.data[column] = label_encoder.fit_transform(self.data[column])
                
        # Split the dataset into features and target
        X = self.data.drop("Machine failure", axis=1)
        y = self.data["Machine failure"]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        mlflow.start_run()

        # Create a logistic regression classifier
        model = LogisticRegression(random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        #print("Accuracy:", accuracy)
        
        return accuracy


def give_back_the_response(type, air_temp, proc_temp, rot_temp, torque, tool_wear):
    
    the_answer = "failure or not"
    
    return the_answer
    


def test_predictive_maintaincence():
    
    #I think the model code needs to be 
    #global or become a class, 
    # so I can use it in other functions

    # Load the dataset
    data = pd.read_csv("machine_failure.csv")
    
    thing = Model(data)
    result = thing.trained_model()
    
    print("Accuracy:", result)
    
    return result
    '''
    # Convert non-numeric columns to numeric using label encoding
    label_encoder = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == "object":
            data[column] = label_encoder.fit_transform(data[column])

    # Split the dataset into features and target
    X = data.drop("Machine failure", axis=1)
    y = data["Machine failure"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.start_run()

    # Create a logistic regression classifier
    model = LogisticRegression(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Log the parameters and metrics to MLflow
    mlflow.log_params({"test_size": 0.2})
    mlflow.log_metric("accuracy", accuracy)

    # Log the trained model as an artifact
    mlflow.sklearn.log_model(model, "model")

    # End the MLflow run
    mlflow.end_run()
    return accuracy
    
    '''
    
    
if __name__ == "__main__":
    test_predictive_maintaincence()