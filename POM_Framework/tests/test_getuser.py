import json
import pytest
from POM_Framework.utils.api import APIS

@pytest.fixture(scope="module")
def common():
    return APIS()

def test_getuser_validation(common):
    response = common.get('users')
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    print("\n",formatted_json)
    assert response.status_code == 200, "Status code did not match"
    assert len(response.json())>0,"response does not contain any data"
