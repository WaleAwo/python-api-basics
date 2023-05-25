import pytest
import requests

data_set = [
    (1, 'Leanne Graham', 'Romaguera-Crona'),
    (2, 'Ervin Howell', 'Deckow-Crist'),
    (3, 'Clementine Bauch', 'Romaguera-Jacobson'),
    (9, 'Glenna Reichert', 'Yost and Sons')
]


@pytest.mark.parametrize('user_id, name, expected_company_name', data_set)
def test_company_name(user_id, name, expected_company_name):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    body = response.json()

    assert body['name'] == name
    assert body['company']['name'] == expected_company_name
