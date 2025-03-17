import json

class FunctionalParam:
    @staticmethod
    def get_base_end_point():
        with open("D:\API_Automation\POM_Structure2\config\endpoints.json") as json_file:
            properties = json.load(json_file)
            env =  properties["environment"]["env"]
            return properties[env]["base_url"]