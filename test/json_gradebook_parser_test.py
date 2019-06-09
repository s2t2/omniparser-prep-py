import os

from app.json_gradebook_parser import parse_average_grade

def test_latest_closing_price():

    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_previous.json")
    assert parse_average_grade(prev_gradebook_filepath) == 80

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook.json")
    assert parse_average_grade(gradebook_filepath) == 90
