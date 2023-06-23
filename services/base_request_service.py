from support.utilities import Utility
import requests
import json
import jsonschema


class BaseRequestService:

    def __init__(self, pstr_filedescription: str, pstr_endpoint: str):
        self.test_description = Utility().read_service_desc(path=pstr_filedescription, endpoint=pstr_endpoint)
        self.response = None
        self.response_data = None
        self.schema_object = None

    def make_http_request(self):
        try:
            url = self.test_description['target_url'] + self.test_description['endpoint']

            if self.test_description['queryparams'] != "":
                url += self.test_description['queryparams']

            self.response = requests.request(method=self.test_description['method'], url=url, headers=self.test_description['headers'],
                                             data=self.test_description['payload'])

        except Exception as e:
            raise Exception(
                'Exception occurred in BaseRequestService : make_http_request -->' + str(e))

    def check_response_code(self, pstr_return_code: int) -> bool:
        try:
            result = self.response.status_code == pstr_return_code
            return result

        except Exception as e:
            raise Exception(
                'Exception occurred in BaseRequestService : check_response_code -->' + str(e))

    def validate_json_schema(self, path):
        try:
            schema_obj = Utility().read_json_schema(path=path)
            self.response_data = json.loads(self.response.content)
            jsonschema.validate(self.response_data, schema_obj.schema)
            return True

        except jsonschema.exceptions.ValidationError as e:
            print('Exception occurred in BaseRequestService : generate_response_schema -->' + str(e))
            return False
