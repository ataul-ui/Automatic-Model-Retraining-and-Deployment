import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support as score

# Hyperparameter tuning

from hyperopt import tpe, STATUS_OK, Trials, hp, fmin, STATUS_OK, space_eval
import mlflow
import mlflow.sklearn
import json

#LOOK AT INTRO TO AI PROJECT I DID
#TWO YEARS AGO ON HOW TO WRITE ML MODELS
#USING CLASSES
class Model:
    
    instance_created = False
    def __init__(self, data):
        self.data = data
        Model.instance_created = True
    
    def pre_processing(self):
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                self.data[column] = label_encoder.fit_transform(self.data[column])

        X = self.data.drop(["Machine failure", "UDI", "Product ID", "TWF", "HDF", "PWF", "OSF", "RNF", "Type"], axis=1)
        y = self.data["Machine failure"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def training(self):
        
        self.pre_processing()
        '''
        space = {
        #'C': hp.loguniform('C', low=-3, high=3),
        'C': hp.uniform('C', 0.01, 10),
        'penalty': hp.choice('penalty', ['l1', 'l2', 'elasticnet', 'none']),
        'l1_ratio': hp.uniform('l1_ratio', 0, 1),
        #'solver': hp.choice('solver', ['newton-cg', 'lbfgs', 'sag', 'saga']),
        'fit_intercept': hp.choice('fit_intercept', [True, False])
        }'''
        space = {
            'warm_start': hp.choice('warm_start', [True, False]),
            'fit_intercept': hp.choice('fit_intercept', [True, False]),
            'tol': hp.uniform('tol',0.00001,000.1),
            'C': hp.uniform('C', 0.05, 3),
            'solver': hp.choice('solver', ['newton-cg', 'lbfgs', 'sag', 'saga']),
            'max_iter': hp.choice('max_iter', range(100, 1000))
        }

        def objective(params):
            # Extract the 'C' value from the choice index
            #params['C'] = float(params['C'])
            #model = LogisticRegression(random_state=42, max_iter=10000, solver='saga', **params)
            model = LogisticRegression(**params)
            model.fit(self.X_train, self.y_train)
            accuracy = model.score(self.X_test, self.y_test)
            return -accuracy  # Negative accuracy for minimization

        bayes_trial = Trials()
        best = fmin(
            fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=50,
            trials=bayes_trial
        )
        # Convert the 'solver' choice back to string
        best['solver'] = ['newton-cg', 'lbfgs', 'sag', 'saga'][best['solver']]
        # Retrieve the best hyperparameters
        #best_model = LogisticRegression(random_state=42, max_iter=10000, solver='saga', **best)
        best_model = LogisticRegression(**best)
        best_model.fit(self.X_train, self.y_train)

        # Evaluate the best model
        accuracy = best_model.score(self.X_test, self.y_test)
        second_accuracy = best_model.score(self.X_train, self.y_train)

        # Start MLflow experiment
        mlflow.set_experiment("Predictive Maintenance")
        with mlflow.start_run():
            # Log the best hyperparameters
            mlflow.log_params(best)
            # Log the model artifact
            mlflow.sklearn.log_model(best_model, "model")
            # Log the evaluation metrics
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("second_accuracy", second_accuracy)

        return best_model
        
        '''model = LogisticRegression(random_state=42, max_iter=10000, solver='saga')
        # Start MLflow experiment
        mlflow.set_experiment("Predictive Maintenance")
        model.fit(self.X_train, self.y_train)
        
        # Evaluate the model
        accuracy = model.score(self.X_test, self.y_test)
        second_accuracy = model.score(self.X_train, self.y_train)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("second_accuracy", second_accuracy)
    
        # Log the model artifact
        mlflow.sklearn.log_model(model, "model")
        return model'''


    
    def logistic_model_result(self):
        if self.__class__.trained_or_not:
            return "return the model result"
        else:
            self.__class__.trained_or_not = True
            return "train the model, then return the result"
    '''
    def logistic_regression_model(self):
        label_encoder = LabelEncoder()
        for column in self.data.columns:
            if self.data[column].dtype == "object":
                self.data[column] = label_encoder.fit_transform(self.data[column])
        #use this as reference for feature engineering
        # and xgboost building:
        # https://www.kaggle.com/code/yantxx/xgboost-binary-classifier-machine-failure
        #do preprocessig on the data, if machine type 
        # is not M or L, then make it other

        X = self.data.drop(["Machine failure", "UDI", "Product ID", "TWF", "HDF", "PWF", "OSF", "RNF"], axis=1)
        y = self.data["Machine failure"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression(random_state=42, max_iter=10000, solver='saga')
        # Start MLflow experiment
        mlflow.set_experiment("Predictive Maintenance")
        model.fit(X_train, y_train)
        
        # Evaluate the model
        accuracy = model.score(X_test, y_test)
        second_accuracy = model.score(X_train, y_train)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("second_accuracy", second_accuracy)
    
        # Log the model artifact
        mlflow.sklearn.log_model(model, "model")

        return model
    '''
    


def result_return(data_input):
#def result_return():
    
    
    data = pd.read_csv("machine_failure.csv")

    thing = Model(data)
    #result = thing.pre_processing()
    result = thing.training()
    
    

    
    # do feature engineering by reomoving all the unecessary
    # training parameter such as twf hdf, uid, etc

    
    # Parse the JSON data
    data = json.loads(data_input)
    #data = json.loads(json_data)
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)

    # Assuming you have a new data point stored in a DataFrame called 'new_data'
    
    '''label_encoder = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column])'''
    """label_encoder = LabelEncoder()
    for column in df.columns:
        if isinstance(df[column][0], list):
            # Flatten the list and convert it to a single value
            df[column] = [item[0] for item in df[column]]
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column])"""
    label_encoder = LabelEncoder()
    for column in df.columns:
        if isinstance(df[column][0], list):
            # Flatten the list and convert it to a single value
            df[column] = [item[0] for item in df[column]]
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column].astype(str))
        else:
            try:
                df[column] = label_encoder.fit_transform(df[column])
            except TypeError:
                df[column] = label_encoder.fit_transform(df[column].astype(str))

    predictions = result.predict(df)
    '''want_test = pd.DataFrame([0,1])
    if predictions[0] == want_test[0].all():
        print("success")
    elif predictions[0] == want_test[1].all():
        print("whatever")
    else:
        print("what happened?")
    print(predictions[0])'''
    
    
    


    return predictions


if __name__ == "__main__":
    json_code = {
        "Air temperature [K]": [55],
        "Process temperature [K]": [8787.1],
        "Rotational speed [rpm]": [20],
        "Torque [Nm]": [28.6],
        "Tool wear [min]": [9]
    }
    
    if Model.instance_created:
        print("An instance of MyClass has already been created")
    else:
        print("No instance of MyClass has been created yet")

    
    json_data = json.dumps(json_code)
    the_answer = result_return(json_data)
    want_test = pd.DataFrame([0,1])
    '''
    print(want_test[0][1])
    print("anoth")
    return "nothig"
    
    '''
    if the_answer[0] == want_test[0][0]:
        print("machine will fail")
    elif the_answer[0] == want_test[0][1]:
        print("machine will continue to work") 
    else:
        print("There is an error somewhere in the code")
    