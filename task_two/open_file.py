import json

from task_two.role_model import Role


def open_file():
    with open("example.json", "r") as my_file:
        example_json = my_file.read()
        return json.loads(example_json)


def role_list():
    valuesList = []
    dict_file = open_file()
    for item in dict_file["data"]["items"]:
        valuesList.append(Role(name=item['name'], id=item['id'], description=item['description']))
    return valuesList

# как из словаря вытащить список айтемс по ключу
#внутри аппенд я должна добавлять обьект класса Role с заполнеными атрибутами из словарей внутри списка ^ из 1го
#пункта

