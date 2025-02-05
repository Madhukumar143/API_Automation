from datetime import datetime

import requests

header = {
    "Accept" : "text/plain",
    "Authorization" : "Bearer a60af206e8ae3de03cc7643e911b262ec2a86b05b7fa946ed5978005eac29743"
}


def generate_email_with_timestamp():  # Fixed spelling of 'generate'
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "madhu" + time_stamp + "@Gmail.com"

payload ={
    "name":"Madhu Virat",
    "gender":"male",
    "email":generate_email_with_timestamp(),
    "status":"active"
}


url = "https://gorest.co.in/public/v2/users"

post_request = requests.post(url,headers=header,json=payload)

response = post_request.json()
print("below is the Post Api response")
print(response)
assert post_request.status_code == 201,"status code is not matching"

get_call = requests.get(url+'/'+str(response["id"]),headers=header)

print("below is the get Api response")
print(get_call.json())