import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com"

class TestJsonPlaceholder:

    # Function that creates a resource and validates the response.
    def test_create_resource(self):
        url = f"{base_url}/posts"
        data = {
            "title": "sample title",
            "body": "sample body",
            "ID": "101"
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=data, headers=headers)

        assert response.status_code == 201
        assert "id" in response.json()


    # Function to update a resource and validates the response.
    def test_update_resource(self):
        url = f"{base_url}/posts/1"
        data = {
            "title": "Updated title",
            "body": "Updated body"
        }
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.put(url, json=data, headers=headers)

        assert response.status_code == 200


    # Function to fetch ID for a given user title.
    def test_fetch_user_id(self):

        url = f"{base_url}/posts"
        params = {
            "title": "sample title"
        }

        response = requests.get(url, params=params)

        assert response.status_code == 200
        assert "id" in response.json()[0]

    # Function to fetch data for a given user ID.
    def test_fetch_user_data(self):

        url = f"{base_url}/users/1"

        response = requests.get(url)

        assert response.status_code == 200
        assert "id" in response.json()

    # Function to fetch comments of a given post
    def test_fetch_comments(self):

        url = f"{base_url}/posts/1/comments"

        response = requests.get(url)

        assert response.status_code == 200
        assert len(response.json()) > 0