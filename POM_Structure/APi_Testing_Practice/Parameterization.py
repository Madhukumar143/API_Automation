import requests

params = {
    "page" : 1,
    "per_page" : 3
}

url = "https://gorest.co.in/public/v2/users"

get_api_call = requests.get(url,params=params)
response = get_api_call.json()
print(response)