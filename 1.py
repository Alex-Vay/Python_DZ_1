import requests

BASE_URL = "https://fakestoreapi.com/"
res = requests.get(f"{BASE_URL}/products")
res = res.json()
for i in res:
    if i['price'] < 20:
        print(i)