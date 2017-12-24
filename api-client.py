#! /usr/bin/env python3

import requests
import json

IP = '172.20.10.10'
API_URL = 'http://'+IP+':5000'

def get_repairs():
    url = API_URL+'/repairs'
    try:
        params = {}

        repairs = requests.get(url, params=params, timeout=(2, 5)).json()
        return repairs

    except Exception as e:
        print(e)


def get_repair(num_rep, jwtoken):
    url = API_URL+'/repair/'+str(num_rep)
    token = "JWT " + jwtoken
    try:
        params = {}
        headers = {'Authorization': token}
        repair = requests.get(url,
                              params=params,
                              headers=headers, 
                              timeout=(2, 5)
                             ).json()
        return repair

    except Exception as e:
        print(e)


def post_authentication(username, password):
    url = API_URL + '/auth'
    data = json.dumps({"username": username, "password": password})
    headers = {"Content-Type": "application/json"}
    
    r = requests.post(url, 
                      data=data,
                      headers=headers,
                      timeout=(2,5)
                      )
    response = r.json()
    return response['access_token']    #set token value
    

print("Repairs: ", get_repairs())
print("---")
my_new_jwt = post_authentication("victor", "1234")
print("JWT: ", my_new_jwt)
print("---")
print("Repair number 1234:", get_repair(1234, my_new_jwt))
print("---")

