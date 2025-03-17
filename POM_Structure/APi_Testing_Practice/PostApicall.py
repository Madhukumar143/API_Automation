import requests

header = {
    "Accept" : "text/plain",
    "content-type" : "application/json"
}

request_body = {
  "id": 1718,
  "title": "string",
  "dueDate": "2025-02-04T04:47:30.372Z",
  "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=header,json=request_body)

print(response.status_code)
response_data = response.json()

assert response.status_code == 200,"Status code did not match"
assert response_data["id"]==1718,"id is not matching"