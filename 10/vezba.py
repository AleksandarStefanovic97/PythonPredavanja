import json


def load_file(file_name):
    with open(file_name, 'r') as file:
        products = json.load(file)
        return products


data = load_file("data/products.json")
print(data)