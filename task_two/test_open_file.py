from task_two.open_file import open_file, role_list
from task_two.role_model import Role


def test():
    assert open_file() == {
        "data": {
            "items": [
                {
                    "name": "name 1",
                    "id": 123456,
                    "description": "Описание 1"
                },
                {
                    "name": "name 2",
                    "id": 654321,
                    "description": "Описание 2"
                },
                {
                    "name": "name 3",
                    "id": 987654,
                    "description": "Описание 3"
                }
            ]
        },
        "total": 3
    }


def test_role_list():
    assert role_list() == [
        Role(name='name 1', id=123456, description='Описание 1'),
        Role(name='name 2', id=654321, description='Описание 2'),
        Role(name='name 3', id=987654, description='Описание 3')
    ]


def test_role_list2():
    dict_file = open_file()
    items = dict_file["data"]["items"]
    data = dict_file.get("data")
    items = data.get("items")
    print(items[1].get("name"))
