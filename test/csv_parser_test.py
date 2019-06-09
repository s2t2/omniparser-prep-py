import os

from app.csv_parser import calculate_average_grade

def test_calculate_average_grade():

    prev_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2018.csv")
    assert os.path.isfile(prev_gradebook_filepath)
    assert calculate_average_grade(prev_gradebook_filepath) == 83.64

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    assert os.path.isfile(gradebook_filepath)
    assert calculate_average_grade(gradebook_filepath) == 90.64
