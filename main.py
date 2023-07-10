'''

import argparse
import logging
import pathlib
import wandb
#import requests
import tempfile


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

#change something here
def go(args):

    # Derive the base name of the file from the URL
    basename = pathlib.Path(args.file_url).name.split("?")[0].split("#")[0]

    # Download file, streaming so we can download files larger than
    # the available memory. We use a named temporary file that gets
    # destroyed at the end of the context, so we don't leave anything
    # behind and the file gets removed even in case of errors
    logger.info(f"Downloading {args.file_url} ...")
    with tempfile.NamedTemporaryFile(mode='wb+') as fp:

        logger.info("Creating run exercise_2")
        with wandb.init(project="exercise_2", job_type="download_data") as run:
            # Download the file streaming and write to open temp file
            with requests.get(args.file_url, stream=True) as r:
                for chunk in r.iter_content(chunk_size=8192):
                    fp.write(chunk)

            # Make sure the file has been written to disk before uploading
            # to W&B
            fp.flush()

            logger.info("Creating artifact")
            artifact = wandb.Artifact(
                name=args.artifact_name,
                type=args.artifact_type,
                description=args.artifact_description,
                metadata={'original_url': args.file_url}
            )
            artifact.add_file(fp.name, name=basename)

            logger.info("Logging artifact")
            run.log_artifact(artifact)

            artifact.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download a file and upload it as an artifact to W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--file_url", type=str, help="URL to the input file", required=True
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the artifact", required=True
    )

    parser.add_argument(
        "--artifact_description",
        type=str,
        help="Description for the artifact",
        required=True,
    )

    args = parser.parse_args()

    go(args)
    
'''


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
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

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

# Create a logistic regression classifier
model = LogisticRegression(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
