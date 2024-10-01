import requests

BASE_URL = "https://fakestoreapi.com/"
res = requests.get(f"{BASE_URL}/users")
for i in res.json():
    print(i)
