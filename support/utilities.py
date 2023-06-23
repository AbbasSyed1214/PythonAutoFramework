import json

import yaml
import os
import jsonschema
from pathlib import Path


class Utility:

    def __init__(self):
        self.service_desc_path = os.path.join(Path(__file__).parent.parent, "services")

    def read_service_desc(self, path: str, endpoint: str) -> dict:
        yml_file = os.path.join(self.service_desc_path, "services_description", path)
        with open(yml_file, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data[endpoint]
            except Exception as e:
                raise Exception(
                    'Exception occurred in Utility : read_service_desc -->' + str(e))

    def read_json_schema(self, path: str) -> dict:
        schema_path = os.path.join(self.service_desc_path, "json_schema", path)
        try:
            with open(schema_path, "r") as schema_file:
                schema_data = jsonschema.Draft7Validator(json.load(schema_file))
                return schema_data

        except Exception as e:
            raise Exception(
                'Exception occurred in Utility : read_json_schema -->' + str(e))

