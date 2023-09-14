import requests

ENDPOINT = 'https://hngtask11011.pythonanywhere.com/api/'  # Replace with your API endpoint URL

# Define a list of HTTP methods you want to test
http_methods = ['GET', 'POST', 'PUT', 'DELETE']


def getAllUsers():
    # gets all the person objects in the database
    response = requests.get(ENDPOINT)
    return response.json()


def getSinglePerson():
    # test GET method for user_ids from 5 to 30
    responses1 = []
    for id in range(5, 30):
        responses1.append(requests.get(ENDPOINT + str(id)).json())
    return responses1


def createPerson():
    responses2 = []
    data_to_send = [
        {"name": "Guy French"},
        {"name": "Marcus Hertz"},
        {"name": "Frenkie Gillingam"},
        {"name": "Sam Gillingam"},
    ]
    for data in data_to_send:
        responses2.append(requests.post(ENDPOINT, data=data).json())
    return responses2


def updatePerson():
    responses3 = []
    data_to_send = [
        {'7': {"name": "Samuel Gillingam"}, },
        {'9': {"name": "John English"}, },
        {'1': {"name": "Ezekiel Okebule Smithson"}, },
        {'90': {"name": "Samuel Maxwell"}, },
    ]
    for data in data_to_send:
        sub = ''.join([key for key in data.keys()])
        responses3.append(requests.put(ENDPOINT + sub, data=data[sub]).json())
    return responses3


def deletePerson(id):
    response = requests.delete(ENDPOINT + str(id))
    return response.json()


for method in http_methods:
    if method == 'GET':
        print("--------All Users----------\n")
        print(getAllUsers(), "\n")
        print("--------Specific Users ----------\n")
        print(getSinglePerson())
    elif method == 'POST':
        print("The following users would be created:\n")
        print(createPerson())
        print("Users Created\n")
    elif method == 'PUT':
        print("The following users would be updated:\n")
        print(updatePerson())
        print("Users Updated\n")
    elif method == 'DELETE':
        print(deletePerson(8))
        print("person deleted")
