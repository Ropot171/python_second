import json


def open_file():
    with open("example.json", "r") as my_file:
        example_json = my_file.read()
        return json.loads(example_json)
