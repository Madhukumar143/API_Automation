import random


class CommonUtility:
    @staticmethod
    def get_custom_header():
        header = {"Authorization": "Bearer a60af206e8ae3de03cc7643e911b262ec2a86b05b7fa946ed5978005eac29743",
                  "Content-Type" : "application/json"}
        return header

    @staticmethod
    def get_unique_email():
        data = random.randint(1,10000)
        email = f"test_api{data}@gmail.com"
        return email