#! /usr/bin/env python3

import requests

def get_repairs():
    api_URL = 'http://127.0.0.2:5000'
    try:
        params = {}

        json_data = requests.get(api_URL, params=params, timeout=(2, 5)).json()
        return json_data

    except Exception as e:
        print(e)


get_repairs()
