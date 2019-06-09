import os
import csv
import statistics

def calculate_average_grade(my_csv_filepath):
    return 80

if __name__ == "__main__":

    #
    # CAPTURE USER INPUTS
    #

    year = input("Please select a year (2018 or 2019):")

    if year not in ["2018", "2019"]:
        print("OH, INVALID SELECTION. PLEASE TRY AGAIN...")
        exit()

    print("SELECTED YEAR:", year)

    #
    # PROCESS DATA AND DISPLAY OUTPUTS
    #

    selected_filepath = os.path.join(os.path.dirname(__file__), "..", "data", f"gradebook_{year}.csv")
    print("PARSING A LOCAL CSV FILE:", selected_filepath)

    if not os.path.isfile(selected_filepath):
        print("OH, THAT FILE DOESN'T EXIST. PLEASE PLACE A FILE THERE OR CHECK YOUR FILEPATH...")
        exit()

    average_grade = calculate_average_grade(selected_filepath)

    print("AVERAGE GRADE:", average_grade)
