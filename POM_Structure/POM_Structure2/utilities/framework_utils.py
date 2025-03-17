import pytest
import requests


class FrameworkUtils:
    @staticmethod
    def fire_api_with_custom_headers(request_method="GET",
                                     request_url=None,
                                     request_param = None,
                                     request_json=None,
                                     headers = None,
                                     expected_status_code = 200):
        response = requests.request(request_method,
                               request_url,
                               params = request_param,
                               json =request_json,
                               headers=headers)
        try:
            assert response.status_code == expected_status_code,\
                f"API call failed status code is {expected_status_code} but found is {response.status_code}"
            return response
        except:
            pytest.fail("api call failed")
