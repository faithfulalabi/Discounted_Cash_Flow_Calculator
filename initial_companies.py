import helpers


API_KEY = ""
API_URL = "https://financialmodelingprep.com"
TICKER_TYPE = str
COMPANY_DATA_TYPE = dict


def get_length_of_data(ticker: str):
    """make request for companies historical income statement data and returns
    the company ticker and the number of years of history they have"""
    response = {}
    key = "request_status"
    income_statement_data = helpers.get_income_statement_data(
        api_service_url=API_URL, ticker=ticker, api_key=API_KEY
    )
    request_status = next(filter(lambda d: d.get(key), income_statement_data), None)
    error_stat = request_status.get("request_status", "")
    if error_stat != "":
        if error_stat == "ERROR":
            response["company"] = ticker
            response["num_of_years"] = 0
            response["status_code"] = "ERROR"
            return response

        elif error_stat == "OK":
            response["company"] = ticker
            response["num_of_years"] = len(income_statement_data)
            response["status_code"] = "OK"
            return response


def evaluate_company(company_data: COMPANY_DATA_TYPE):
    """Take in companies data and pass or deny based on length of companies history"""
    response = {}
    status_code = company_data.get("status_code", "")
    if status_code != "":
        if status_code == "OK":
            num_of_years = company_data.get("num_of_years")
            companies_ticker = company_data.get("company")
            if num_of_years >= 5:
                response["company"] = companies_ticker
                response["num_of_years"] = num_of_years
                response["note"] = f"Company satisfies requirement {companies_ticker}"
                print(f"Company satisfies requirement {companies_ticker}")
                return response
            else:
                response["company"] = companies_ticker
                response["num_of_years"] = num_of_years
                response[
                    "note"
                ] = f"Company does not satisfies requirement {companies_ticker}"
                print(f"Company does not satisfies requirement {companies_ticker}")
                return response


if __name__ == "__main__":
    ticker = "TSLA"
    company_data = get_length_of_data(ticker=ticker)
    response = evaluate_company(company_data=company_data)
    print(response)
