import requests
import pytest
from config import base_url


# Function to update a resource and validates the response.
def update_resource(id, name, age):
    url = f"{base_url}/posts/{id}"
    js = {
        "Name": name,
        "Age": age
    }

    headers = {
        "Content-Type" : "application/json"
    }

    response = requests.put(url = url, json=js, headers=headers)
    # print(response.json())
    # print(response.status_code)

    if response.status_code == 200:
        print("Resource updated Successfully")
    else:
        print("Failed to update the resources")



# name = "romi"
# age = 23
# id = 1
#
# update_resource(id, name, age)