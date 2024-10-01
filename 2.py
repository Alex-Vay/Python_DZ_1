import requests

BASE_URL = "https://fakestoreapi.com/"
res = requests.get(f"{BASE_URL}/products/categories")
print("\n".join(res.json()))