import json

import requests


# GET
def test_get_request():
    users_get_response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    print("Response status code: {}".format(users_get_response.status_code))
    print("Response headers: {}".format(users_get_response.headers['content-type']))
    print("Response body: {}".format(json.dumps(users_get_response.json(), indent=4)))


# POST
def test_post_request():
    post_data = {
        'title': 'The Car and the Moon',
        'body': 'This is a story about a car and a moon.',
        'userId': '1'
    }

    posts_post_request = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
    print("Response status code: {}".format(posts_post_request.status_code))
    print("Response body: {}".format(json.dumps(posts_post_request.json(), indent=4)))


# PUT
def test_put_request():
    put_data = {
        'title': 'The Car and the Sun',
        'body': 'This is a story about a car and a moon.',
        'userId': '1',
        'id': 1
    }

    posts_put_request = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=put_data)
    print("Response status code: {}".format(posts_put_request.status_code))


# PATCH
def test_patch_request():
    patch_data = {
        'body': 'This is a story about a car and a moon.'
    }

    posts_patch_request = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=patch_data)
    print("Response status code: {}".format(posts_patch_request.status_code))


# DELETE
def test_delete_request():
    posts_delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

    print("Response status code: {}".format(posts_delete_response.status_code))
    print("Response headers: {}".format(posts_delete_response.headers['content-type']))
