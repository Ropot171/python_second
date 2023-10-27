from task_two.open_file import open_file


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


