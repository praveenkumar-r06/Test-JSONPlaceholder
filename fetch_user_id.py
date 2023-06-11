import requests
import pytest
from config import base_url

def fetch_user_id(title):
    url = f"{base_url}/posts"
    param = {
        "Title" : title
    }

    response = requests.get(url, params=param)
    if response.status_code == 200:
        data = response.json()
        if data:
            user_id = data[0]["userId"]
            print(f"user_ID for the {title} is {user_id}")
        else:
            raise ValueError("Title not found")
    else:
        raise ValueError("Failed to fetch the user ID from title")



# title = 'nomi'
#
# fetch_user_id(title)