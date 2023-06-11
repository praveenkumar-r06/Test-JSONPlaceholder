import requests
import pytest
from config import base_url

# Function to fetch comments of a given post
def fetch_comments(id):
    url = f"{base_url}/posts/{id}/comments"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        print(comments)
        num_comments = len(comments)
        print(f"Number of comments for {id} is {num_comments}")

    else:
        raise ValueError("Failed to fetch comments")


# fetch_comments(1)