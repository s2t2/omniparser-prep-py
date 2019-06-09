import os

from app.stock_prices_parser import latest_closing_price, to_usd

def test_processing_of_user_inputs():
    assert "goog".upper() == "GOOG"
    assert "GOOG".lower() == "goog"

def test_latest_closing_price():

    msft_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "daily_prices_msft.json")
    assert latest_closing_price(msft_filepath) == "131.4000"

    aapl_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "daily_prices_aapl.json")
    assert latest_closing_price(aapl_filepath) == "190.1500"

    goog_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "daily_prices_goog.json")
    assert latest_closing_price(goog_filepath) == "1066.0400"

def test_to_usd():
    # it should apply USD formatting:
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places:
    assert to_usd(4.5) == "$4.50"

    # it should round to two places:
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators:
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

    # it wants you to convert a string to a float before passing the value in:
    assert to_usd(float("131.4000")) == "$131.40"
