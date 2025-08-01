'''
USAGE:fetch all users
API URL:https://jsonplaceholder.typicode.com/users
Method:GET
Required Fields: None
Access Type:Public
'''
import requests
api_url='https://jsonplaceholder.typicode.com/users'
response=requests.get(api_url)
print(response)

users=response.json()
print(users)