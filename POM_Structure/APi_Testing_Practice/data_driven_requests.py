import requests
import json

header = {
    "Accept" : "text/plain",
    "Authorization" : "Bearer a60af206e8ae3de03cc7643e911b262ec2a86b05b7fa946ed5978005eac29743"
}

base_url = "https://reqres.in/"

load_data = open('payload.json')
payload = json.load(load_data)

post_request = requests.post(base_url+"api/users",headers=header,json=payload)

response = post_request.json()
print("below is the Post Api response")
print(response)
assert post_request.status_code == 201,"status code is not matching"

get_call = requests.get(base_url+'api/users/'+str(response["id"]),headers=header)
print(base_url+'api/users/'+str(response["id"]))
print("below is the get Api response")
print(get_call.json())