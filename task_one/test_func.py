from first_func import func
from first_func import func_req


def test():
    assert func(5, 8) == 13
    assert func(5, 9) == 14


def test_url():
    url_address = 'https://scotch.io'
    assert func_req(url_address).status_code == 200