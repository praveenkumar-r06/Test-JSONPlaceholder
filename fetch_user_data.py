import requests
import pytest
from config import base_url

# Function to fetch data for a given user.
def fetch_user_data(id):
    url = f"{base_url}/posts/{id}"

    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"User Data: {user_data}")
    else:
        print(f"Failed to fetch user data. Error: {response.text}")


# id = 100
#
# fetch_user_data(id)