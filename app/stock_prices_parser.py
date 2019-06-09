from pprint import pprint
import os
import json

def to_usd(my_price):
    """
    converts a numeric value to usd-formatted string, for printing and display purposes
    """
    return "${0:,.2f}".format(my_price) #> $12,000.71

def latest_closing_price(my_json_filepath):

    with open(my_json_filepath, "r") as json_file:
        file_contents = json_file.read()

    daily_prices = json.loads(file_contents)

    latest_date = daily_prices["Meta Data"]["3. Last Refreshed"]

    latest_prices = daily_prices["Time Series (Daily)"][latest_date]

    latest_close = latest_prices["4. close"] #> '1066.0400'

    return latest_close

if __name__ == "__main__":

    #
    # CAPTURE USER INPUTS
    #

    selected_symbol = input("Please select a stock symbol ('AAPL', GOOG', or 'MSFT'):")

    if selected_symbol.upper() not in ["AAPL", "GOOG", "MSFT"]:
        print("OH, INVALID SELECTION. PLEASE TRY AGAIN...")
        exit()

    print("SELECTED SYMBOL:", selected_symbol.upper())

    #
    # PROCESS DATA AND DISPLAY OUTPUTS
    #

    selected_filepath = os.path.join(os.path.dirname(__file__), "..", "data", f"stock_prices_{selected_symbol.lower()}.json")
    print("PARSING A LOCAL JSON FILE:", selected_filepath)

    if not os.path.isfile(selected_filepath):
        print("OH, THAT FILE DOESN'T EXIST. PLEASE PLACE A FILE THERE OR CHECK YOUR FILEPATH...")
        exit()

    latest_close = latest_closing_price(selected_filepath)
    print("LATEST CLOSING PRICE:", to_usd(float(latest_close)))
