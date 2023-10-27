import requests


def func(a: int, b: int):
    result = a + b
    return result


def func_req(url: str):
    url_text = requests.get(url)
    return url_text