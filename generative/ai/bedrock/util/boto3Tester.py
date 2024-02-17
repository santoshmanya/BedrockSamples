import json
import os
import sys

import boto3

module_path = ".."
sys.path.append(os.path.abspath(module_path))
import bedrock

# ---- ⚠️ Un-comment and edit the below lines as needed for your AWS setup ⚠️ ----

# os.environ["AWS_DEFAULT_REGION"] = "<REGION_NAME>"  # E.g. "us-east-1"
# os.environ["AWS_ACCESS_KEY_ID"] = "Axxxxxxxxxxxxxxxxx"
# os.environ["AWS_SECRET_ACCESS_KEY"] = "xxxxxxxxxxxxxxxx"  # E.g. "us-east-1"




boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None),
    runtime=False
)

# dont forget to enable  models in AWS Bedrock Model Access
#https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess
response = boto3_bedrock.list_foundation_models()

print(response)


