from googleapiclient.discovery import build
import base64
import google.auth
import os

def hello_pubsub():   
 
    service = build('dataflow', 'v1b3')
    project = "valid-verbena-437709-h5"

    template_path = "gs://dataflow-templates-us-east1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "dataflow-bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricket-analysis/udf.js",
        "JSONPath": "gs://cricket-analysis/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "valid-verbena-437709-h5.cricket_analysis.batsmen-ranking",
        "inputFilePattern": "gs://cricket-analysis/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataops-dataflow-2024/temp",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

hello_pubsub()