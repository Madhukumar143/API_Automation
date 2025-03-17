import json

from win32com.demos.dump_clipboard import formats

from POM_Structure2.config.api_config import ApiUrls
from POM_Structure2.functional_api_test.functional_param import FunctionalParam
from POM_Structure2.req_res.request.gorest import GoRest
from POM_Structure2.utilities.common_utils import CommonUtility
from POM_Structure2.utilities.framework_utils import FrameworkUtils


def test_api_chaining():
    url = FunctionalParam.get_base_end_point()
    #print("Get url = ",ApiUrls.get_user_by_id("2"))
    GET_USER_URL = ApiUrls.GET_USER
    header = CommonUtility.get_custom_header()
    random_email = CommonUtility.get_unique_email()
    #print("getting json request")
    json_request = GoRest.CREATE_USER
    json_request["email"]=random_email
    #print(json_request)
    """response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                request_url=GET_USER_URL,
                                                headers=header)
    print(response.json())"""
    post_response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                                request_url=GET_USER_URL,
                                                                headers=header,
                                                                request_json=json_request,
                                                                expected_status_code=201)
    format= post_response.json()
    user_id = format["id"]
    #print("user id is -> ",user_id)
    formatted_json = json.dumps(format, indent=4)
    #print(formatted_json)
    GET_USER_ID_URL = ApiUrls.get_user_by_id(user_id)
    #print("GET_USER_ID_URL",GET_USER_ID_URL)
    res = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                      request_url=GET_USER_ID_URL,
                                                      headers=header)
    final_user_id = res.json()["id"]
    formats= res.json()
    test = json.dumps(formats,indent = 4)
    print(test)

    assert user_id == final_user_id , "user id did not match"
