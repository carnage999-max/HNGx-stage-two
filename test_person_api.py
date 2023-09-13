import requests

#ENDPOINT = 'https://hngtask11011.pythonanywhere.com/api/'  # Replace with your API endpoint URL
ENDPOINT = '127.0.0.1:8000/api'
# Define a list of HTTP methods you want to test
http_methods = ['GET', 'POST', 'PUT', 'DELETE']

responses = []

def getAllUsers():
    #gets all the person objects in the database
    response = requests.get(ENDPOINT)
    return print(response.json())

def getSinglePerson():
    # test GET method for user_ids from 5 to 30
    for id in range(5, 30):
        responses.append(requests.get(ENDPOINT + str(id)).json())
    print(responses)

def createPerson():
    data_to_send = {
        {"name": "John French"},
        {"name": "Frank Hertz"},
        {"name": "Robert Gillingam"},
        {"name": "David Gillingam"}
    }
    for data in data_to_send:
        responses.append(requests.post(ENDPOINT, data=data))
    print(responses)

for method in http_methods:
    if method == 'GET':
        getAllUsers()
        getSingleUser()
    elif method == 'PUT':
        data_to_send = {'key1': 'updated_value1', 'key2': 'updated_value2'}  # Data for PUT request
        response = requests.put(ENDPOINT, json=data_to_send)
    elif method == 'DELETE':
        response = requests.delete(ENDPOINT)

    # Handle the response
    # if response.status_code == 200:
    #     print(f"{method} request was successful")
    #     response_data = response.json()
    # else:
    #     print(f"{method} request failed with status code: {response.status_code}")
