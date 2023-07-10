


'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
import wandb

# Load the dataset
data = pd.read_csv("machine_failure.csv")

# Split the dataset into features and target
X = data.drop("Machine failure", axis=1)
y = data["Machine failure"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Start MLflow experiment
mlflow.set_experiment("Predictive Maintenance")

with mlflow.start_run() as run:
    # Log parameters and dataset information
    mlflow.log_params({"n_estimators": model.n_estimators})
    mlflow.log_param("test_size", 0.2)
    # mlflow.log_dataset_info(X=X_train, y=y_train, data_format="csv")
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)
    
    # Log the model artifact
    mlflow.sklearn.log_model(model, "model")
    
    # Initialize Wandb
    wandb.init(project="Predictive Maintenance", sync_tensorboard=True)
    
    # Log experiment to Wandb
    wandb.log({"accuracy": accuracy})

    # Save the experiment run ID for future reference
    run_id = run.info.run_id

# Log MLflow and Wandb experiment links
mlflow_link = f"https://mlflow.server.com/experiments/{run.info.experiment_id}/runs/{run_id}"
wandb_link = wandb.run.get_url()
print(f"MLflow experiment link: {mlflow_link}")
print(f"Wandb experiment link: {wandb_link}")
'''
'''import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn

def test_predictive_maintaincence():

    # Load the dataset
    data = pd.read_csv("machine_failure.csv")

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
    
    
if __name__ == "__main__":
    pytest.main()  '''