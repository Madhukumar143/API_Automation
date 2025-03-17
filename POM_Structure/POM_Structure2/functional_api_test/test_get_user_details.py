import pytest

from POM_Structure2.config.api_config import ApiUrls
from POM_Structure2.functional_api_test.functional_param import FunctionalParam
from POM_Structure2.req_res.request.gorest import GoRest
from POM_Structure2.utilities.common_utils import CommonUtility
from POM_Structure2.utilities.framework_utils import FrameworkUtils


class Testgetuser:
    @pytest.mark.getuser
    def test_get_user_details(self):
        GET_USER_URL = ApiUrls.GET_USER
        header = CommonUtility.get_custom_header()
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url = GET_USER_URL,
                                                               headers = header)
        print(response.json())
        print("API success")

    @pytest.mark.createuser
    def test_create_user(self):
        GET_USER_URL = ApiUrls.GET_USER
        header = CommonUtility.get_custom_header()
        json_req = GoRest.CREATE_USER
        random_email = CommonUtility.get_unique_email()
        json_req["email"] = random_email
        response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                               request_url=GET_USER_URL,
                                                               headers=header,
                                                               request_json=json_req,
                                                               expected_status_code=201)
        print(response.json())
        print("API success")