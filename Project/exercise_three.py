import requests


def test_response_body():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    body = response.json()

    assert body['name'] == 'Leanne Graham'
    assert body['address']['street'] == 'Kulas Light'
    assert body['company']['name'] == 'Romaguera-Crona'


def test_response_body_list():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    body = response.json()

    assert body[1]['name'] == 'Ervin Howell'
    assert body[7]['company']['name'] == 'Abernathy Group'
