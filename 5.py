import json

import requests

BASE_URL = "https://fakestoreapi.com/"
user = {
    'email':'John@gmail.com',
    'username':'Alex',
    'password':'m38rmF$',
    'name':{
        'firstname':'Alex',
        'lastname':'Doe'
    },
    'address':{
        'city':'kilcoole',
        'street':'7835 new road',
        'number':3,
        'zipcode':'12926-3874',
        'geolocation':{
            'lat':'-37.3159',
            'long':'81.1496'
        }
    },
    'phone':'1-570-236-7033'
}

res = requests.post(f"{BASE_URL}/users", json=user)
print(res.json())
