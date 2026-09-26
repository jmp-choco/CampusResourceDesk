import json

FILE_PATH = "data/resources.json"


def load_resources():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_resources(resources):
    with open(FILE_PATH, "w") as file:
        json.dump(resources, file, indent=4)