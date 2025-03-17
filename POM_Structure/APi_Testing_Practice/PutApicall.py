import requests

#Header for get call
head = {
    "Accept" : "text/plain",
}
#Header for Put call
put_header = {
    "Accept": "text/plain",
    "content-type": "application/json"
}

get_call = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/17",headers=head)
print("before Editing")
#print response of get Api
print(get_call.json())

#Put Api request body
update_request_body = {
  "id": 17,
  "title": "madhu",
  "dueDate": "2025-02-04T05:11:09.085Z",
  "completed": True
}

put_call = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/17",headers=put_header,json=update_request_body)

print("after Editing")
#print response of put api
print(put_call.json())

