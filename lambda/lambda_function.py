import json
import boto3
import time
import logging

cw = boto3.client('cloudwatch')
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)

def lambda_handler(event, context):
    # --- CORS Preflight Handling ---
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "https://mysurveysite.s3.us-east-1.amazonaws.com",
                "Access-Control-Allow-Methods": "POST,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type,x-api-key"
            },
            "body": ""
        }

    # --- Main Request Handling ---
    start_time = time.time()

    try:
        body_str = event.get("body", "{}")
        body = json.loads(body_str)
    except json.JSONDecodeError as e:
        LOG.error(f"JSON decode error: {e}")
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "https://mysurveysite.s3.us-east-1.amazonaws.com"
            },
            "body": "Invalid JSON format in request body."
        }

    print("Received survey submission:", body)

    log_message = {
        "submission_time": time.time(),
        "survey_data": body,
        "latency": time.time() - start_time
    }
    LOG.info(json.dumps(log_message))

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "https://mysurveysite.s3.us-east-1.amazonaws.com",
            "Access-Control-Allow-Methods": "POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,x-api-key"
        },
        "body": "Survey submitted and logs created!"
        
    }
