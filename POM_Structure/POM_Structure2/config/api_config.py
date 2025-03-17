from POM_Structure2.functional_api_test.functional_param import FunctionalParam


class ApiUrls:
    GET_USER = FunctionalParam.get_base_end_point()+"/public/v2/users"
    @staticmethod
    def get_user_by_id(user_id):
        return FunctionalParam.get_base_end_point()+f"/public/v2/users/{user_id}"

