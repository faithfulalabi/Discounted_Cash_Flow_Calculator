import os
import json
import boto3
import requests
from http import HTTPStatus

SERVICE_TYPE = str
REGION_TYPE = str
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)


def create_aws_service(service: SERVICE_TYPE, region: REGION_TYPE):
    service = boto3.resource(
        service_name=service,
        region_name=region,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    return service


def http_response(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, headers=None, body=""):
    """Create a correctly formatted response for the API."""
    if headers is None:
        headers = {
            "Content-Type": "application/json",
        }
    return {
        "isBase64Encoded": False,
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body),
    }


def make_http_request(url: str):
    """Make an HTTP request to the specified URL."""
    status = {"request_status": "ERROR"}
    try:
        req_response = requests.request("GET", url)
        if req_response.status_code == 200:
            response = json.loads(req_response.text)
            if type(response) is dict:
                err_message = response.get("Error Message")
                if err_message != None:
                    print(
                        f"Error within the API occured making the request: {err_message}"
                    )
                    response.update(status)
                    return list(response)
                else:
                    status["request_status"] = "OK"
                    response.update(status)
                    return list(response)
            else:
                status["request_status"] = "OK"
                response.append(status)
                return response
        else:
            status["error_message"] = req_response.text
            status["status_code"] = req_response.status_code
            response = status
            return list(response)
    except Exception as e:
        print(f"Error occured when makeing http request:{e}")


def get_income_statement_data(
    api_service_url: str,
    ticker: str,
    api_key: str,
    period: str = "annual",
):
    """makes request for income statement data default is annually and returns the
    hisotrical income satatement data"""

    api_url = f"{api_service_url}/api/v3/income-statement/{ticker}?period={period}&apikey={api_key}"

    income = make_http_request(url=api_url)

    return income
