"""import json
from POM_Structure2.config.api_config import ApiUrls
from POM_Structure2.functional_api_test.functional_param import FunctionalParam
from POM_Structure2.req_res.request.gorest import GoRest
from POM_Structure2.utilities.common_utils import CommonUtility
from POM_Structure2.utilities.framework_utils import FrameworkUtils


def test_url():
    url = FunctionalParam.get_base_end_point()
    #print("Get url = ",ApiUrls.get_user_by_id("2"))
    GET_USER_URL = ApiUrls.GET_USER
    header = CommonUtility.get_custom_header()
    random_email = CommonUtility.get_unique_email()
    #print("getting json request")
    json_request = GoRest.CREATE_USER
    json_request["email"]=random_email
    #print(json_request)
    response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                request_url=GET_USER_URL,
                                                headers=header)
    print(response.json())
    post_response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                                request_url=GET_USER_URL,
                                                                headers=header,
                                                                request_json=json_request,
                                                                expected_status_code=201)
    format= post_response.json()
    formatted_json = json.dumps(format, indent=4)
    print(formatted_json)
"""