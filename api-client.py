#! /usr/bin/env python3

import requests
import json


def get_repairs():
    api_URL = 'http://localhost:5000/repairs'
    try:
        params = {}

        repairs = requests.get(api_URL, params=params, timeout=(2, 5)).json()
        return repairs

    except Exception as e:
        print(e)


def get_repair(num_rep):
    api_URL = 'http://localhost:5000/repairs/'+str(num_rep)
    try:
        params = {}

        repair = requests.get(api_URL, params=params, timeout=(2, 5)).json()
        return repair

    except Exception as e:
        print(e)


def post_authentication(username, password):
    data = json.dumps({"username": username, "password": password})
    headers = {"Content-Type": "application/json"}
    
    r = requests.post('http://localhost:5000/auth', 
                       data=data,
                       headers=headers,
                       timeout=(2,5)
                       )
    response = r.json()
    return response['access_token']    #set token value
    
    
    #Now you can do authorised calls
    #r = requests.get('http://localhost:5000/protected', 
    #                headers={'Authentication-Token': token})
    #print(r.text)


print("Repairs: ", get_repairs())
print("---")
print("Repair number 1234:", get_repair(1234))
print("---")
my_new_jwt = post_authentication("victor", "1234")
print("JWT: ", my_new_jwt)

print("---")
