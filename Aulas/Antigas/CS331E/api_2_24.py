#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:38:58 2020

@author: mark
"""

import requests
from datetime import datetime

def main():
    git_api()

def api1():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.status_code)
    print(response.json())

def api2():
    parameters = {
        'lat': 30.2672,
        'lon': -97.7431
    }

    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    print(response.status_code)
    print(response.json())

def git_api():

    parameters = {
        'private_token': 'arzRTogqKzsW3-uN2_Hz' # expires 2/25
    }

    project_id = "15055488"

    response = requests.get('https://gitlab.com/api/v4/projects/' + project_id + '/repository/commits', params=parameters)

    print(response.status_code)
    content = response.json()

    for c in content:
        print(c)
    

    


if __name__ == '__main__':
    main()