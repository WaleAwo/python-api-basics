import requests


def test_positive_assertions():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'


def test_negative_assertions():
    response = requests.get("https://jsonplaceholder.typicode.com/users/99")

    assert response.status_code == 404


def test_post_assertion():
    post_data = {
        'title': 'The Car and the Moon',
        'body': 'This is a story about a car and a moon.',
        'userId': '1'
    }

    post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
    assert post_response.status_code == 201
