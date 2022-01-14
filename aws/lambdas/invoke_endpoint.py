import json
import boto3

# Defining the name of the endpoint
ENDPOINT_NAME = 'titanic-byoc-endpoint'

# Establishing the SageMaker runtime client
sagemaker_client = boto3.Session().client('sagemaker-runtime')



def lambda_handler(event, context):
    # Getting the JSON data from the body of the request
    data = json.dumps(json.loads(event['body']))

    # Getting a response from the SageMaker endpoint
    response = sagemaker_client.invoke_endpoint(EndpointName = ENDPOINT_NAME,
                                                ContentType = 'application/json',
                                                Body = data)

    # Returning the response back to the end user
    return {
        'statusCode': 200,
        'body': json.dumps(json.loads(response['Body'].read().decode())
    }
