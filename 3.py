import requests

BASE_URL = "https://fakestoreapi.com/"
res = requests.get(f"{BASE_URL}/products/category/jewelery")
for i in res.json():
    print(i)
# print("\n".join([x["title"] for x in res.json()])) //только наименования