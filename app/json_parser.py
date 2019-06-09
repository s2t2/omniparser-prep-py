
import os

def to_usd(my_price):
    """
    converts a numeric value to usd-formatted string, for printing and display purposes
    """
    return "${0:,.2f}".format(my_price) #> $12,000.71

def latest_closing_price(my_json_filepath):
    return "131.4000"






if __name__ == "__main__":

    selected_symbol = input("Please select a stock symbol ('AAPL', GOOG', or 'MSFT'):")

    if selected_symbol.upper() not in ["AAPL", "GOOG", "MSFT"]:
        print("OH, INVALID SELECTION. PLEASE TRY AGAIN...")
        exit()

    print("SELECTED SYMBOL:", selected_symbol.upper())

    selected_filepath = os.path.join(os.path.dirname(__file__), "..", "data", f"daily_prices_{selected_symbol.lower()}.json")

    print("PARSING A LOCAL JSON FILE:", selected_filepath)

    latest_close = latest_closing_price(selected_filepath)

    print("LATEST CLOSING PRICE:", to_usd(float(latest_close)))
