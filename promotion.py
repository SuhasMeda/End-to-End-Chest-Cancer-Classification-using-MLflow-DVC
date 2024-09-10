from mlflow import MlflowClient
client = MlflowClient()
client.transition_model_version_stage(
    name="clean-bug-447 ", version=3, stage="Production"
)