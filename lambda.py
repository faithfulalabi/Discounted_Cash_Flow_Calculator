import os
import json
from http import HTTPStatus
import initial_companies

import helpers

COMPANY_LOG_QUEUE_URL = ""
AWS_REGION = os.getenv("AWS_REGION", "us")


def send_evaluation_result_to_sqs(evaluation_result):
    """Log the evaluation_result results in an SQS queue for the Testing Data Storage"""
    if COMPANY_LOG_QUEUE_URL:
        sqs_client = helpers.create_aws_service(service="sqs", region=AWS_REGION)
        sqs_response = sqs_client.send_message(
            QueueUrl=COMPANY_LOG_QUEUE_URL,
            MessageBody=json.dumps(evaluation_result),
        )
        if sqs_response.get("ResponseMetadata").get("HTTPStatusCode") != HTTPStatus.OK:
            meta_response = sqs_response.get("ResponseMetadata")
            print(f"Failed to send to sqs {meta_response}")
    else:
        print("Failed to open SQS queue")


def lambda_handler(event, context):

    for ticker in event:
        try:
            company_data = initial_companies.get_length_of_data(ticker=ticker)
            eval_response = initial_companies.evaluate_company(
                company_data=company_data
            )
            note = eval_response.get("note")
            if "Company satisfies requirement" in note:
                send_evaluation_result_to_sqs(evaluation_result=eval_response)
            else:
                print(f"Company did not get uploaded to SQS: {ticker}")
        except Exception as e:
            print(f"Error occured in evaluation lambda handler:{e} ")
