import json
import uuid

import pytest

from POM_Structure.conftest import load_user_data
from POM_Structure.utils.api import APIS

@pytest.fixture(scope="module")
def common():
    return APIS()

def test_getuser_validation(common):
    response = common.get('users')
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
    assert response.status_code == 200, "Status code did not match"
    assert len(response.json())>0,"response does not contain any data"

def test_create_user(common,load_user_data):
    """user_data={
        "name":"madhu",
        "username":"QA User",
        "email":"madhu@test.com"
    }"""
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["email"] = unique_email
    response = common.post('users',user_data)
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
    assert response.status_code == 201, "Status code did not match"
    assert response.json()['name']=="Madhu Kumar", "name does not match in the response"

    response_get = common.get("users").json()
    print(response_get)

def test_update_user(common):
    user_data={
        "name":"madhu",
        "username":"QA User",
        "email":"madhu@test.com"
    }

    response = common.put('users/10',user_data)
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
    assert response.status_code == 200, "Status code did not match"
    assert response.json()['name']=="madhu", "name does not match in the response"
    response_get = common.get("users").json()
    print(response_get)

def test_delete_user(common):
    response = common.delete('users/1')
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
    assert response.status_code == 200, "Status code did not match"

