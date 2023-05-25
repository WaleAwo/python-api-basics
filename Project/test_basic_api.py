import xml.etree.ElementTree as et

import pytest
import requests


def test_status_code_and_content_type():
    response = requests.get("https://api.zippopotam.us/us/90210")

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'


def test_response_body_elements():
    response = requests.get("https://api.zippopotam.us/us/90210")
    body = response.json()  # converts to python dictionary

    assert body['post code'] == '90210'
    assert body['places'][0]['place name'] == 'Beverly Hills'


# data-driven testing
data_set = [
    ('us', '90210', 'Beverly Hills'),
    ('it', '50123', 'Firenze'),
    ('ca', 'B2A', 'North Sydney South Central')
]


@pytest.mark.parametrize('country_code, zip_code, expected_place_name', data_set)
def test_place_names(country_code, zip_code, expected_place_name):
    response = requests.get(f"https://api.zippopotam.us/{country_code}/{zip_code}")
    body = response.json()

    assert body['places'][0]['place name'] == expected_place_name


# token example
def test_with_authorisation():
    response = requests.get("https://api.zippopotam.us/us/90210", headers={'Authorisation': 'Bearer tokenstringhere'})


def test_xml():
    response = requests.get("https://parabank.parasoft.com/parabank/services/bank/accounts/12345")
    xml = et.ElementTree(et.fromstring(response.content))

    assert xml.getroot().tag == 'account'
    assert xml.find('customerId').text == '12212'
