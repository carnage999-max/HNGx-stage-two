import requests

ENDPOINT = 'https://your-api-url.com/endpoint/'  # Replace with your API endpoint URL

# Define a list of HTTP methods you want to test
http_methods = ['GET', 'POST', 'PUT', 'DELETE']

responses = []

for method in http_methods:
    if method == 'GET':
        response = requests.get(ENDPOINT)
    elif method == 'POST':
        data_to_send = [
            {"name": "Theodore Boyle"},
            {"name": "The Black fisherman"},
            {"name": 8}
            ]  # Data for POST request
        for i in data_to_send:
            responses.append(requests.post(ENDPOINT, json=i).json())
        print(responses)
    elif method == 'PUT':
        data_to_send = {'key1': 'updated_value1', 'key2': 'updated_value2'}  # Data for PUT request
        response = requests.put(ENDPOINT, json=data_to_send)
    elif method == 'DELETE':
        response = requests.delete(ENDPOINT)

    # Handle the response
    if response.status_code == 200:
        print(f"{method} request was successful")
        response_data = response.json()
    else:
        print(f"{method} request failed with status code: {response.status_code}")
