# Test-JSONPlaceholder

This repository contains Python scripts for automating interactions with the JSONPlaceholder API (https://jsonplaceholder.typicode.com/). 
The scripts are designed to perform various tasks such as creating a resource, updating a resource, fetching user IDs based on title, fetching user data based on ID and fetching number of line in comments.

Requirements
Python 3.x
Pytest
Requests

The default base URL is set to https://jsonplaceholder.typicode.com.

Execute the desired script:

python create_resource.py

python update_resource.py

python fetch_user_id.py

python fetch_user_data.py

python fetch_number_of_comments.py
The script will perform the specified task and display the results in the console.

Testing

Execute the following command in the terminal:
"pytest test_jsonplaceholder.py"
This will run the pytest script and display the test results.
