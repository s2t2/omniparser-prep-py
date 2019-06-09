import os

from app.gradebook_parser import calculate_average_grade

def test_calculate_average_grade():

    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_previous.json")
    assert calculate_average_grade(prev_gradebook_filepath) == 83.64

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook.json")
    assert calculate_average_grade(gradebook_filepath) == 90.64
