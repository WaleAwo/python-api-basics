import json

import requests

# send request
response = requests.get("https://api.zippopotam.us/us/90210")

# extract response information
print("Response status code: {}".format(response.status_code))
print("Response headers: {}".format(response.headers['content-type']))
print("Response body: {}".format(json.dumps(response.json(), indent=4)))

# payload request
data = {
    'place name': 'London',
    'country': 'UK'
}

# convert python dictionary to json payload
another_response = requests.post('https://api.zippopotam.us/us/90210', json=data)

print("Response status code: {}".format(another_response.status_code))
print("Request payload sent: {}".format(another_response.request.body))
