import os
import json

def parse_average_grade(my_json_filepath):

    with open(my_json_filepath, "r") as json_file:
        file_contents = json_file.read()

    gradebook = json.loads(file_contents)

    return 80

if __name__ == "__main__":

    selected_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook.json")
    print("PARSING A LOCAL JSON FILE:", selected_filepath)

    if not os.path.isfile(selected_filepath):
        print("OH, THAT FILE DOESN'T EXIST. PLEASE PLACE A FILE THERE OR CHECK YOUR FILEPATH...")
        exit()

    average_grade = parse_average_grade(selected_filepath)

    print("AVERAGE GRADE:", avg)
