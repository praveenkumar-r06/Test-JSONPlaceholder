import requests
import pytest
from config import base_url

# base_url = "https://jsonplaceholder.typicode.com"
a = 10

# Function that creates a resource and validates the response.
def create_resource(name, age):
    url = f"{base_url}/posts"
    js = {
        "Name": name,
        "age": age
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=js, headers=headers)
    # print(response.status_code)
    print(response.json())

    if response.status_code == 201:
        print("Resource created successfully")
    else:
        print("Failed to create resource.")




# name = "Gladys"
# age = "32"
# create_resource(name, age)


