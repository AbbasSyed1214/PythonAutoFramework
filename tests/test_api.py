import pytest
from services.base_request_service import BaseRequestService

@pytest.fixture()
def test_object(file_description, endpoint):
    return BaseRequestService(file_description, endpoint)


@pytest.mark.parametrize("file_description, endpoint", [("users.yml", 'json_users')])
def test_json_users_api(test_object):
    test_object.make_http_request()
    assert test_object.check_response_code(200)
    assert test_object.validate_json_schema("users/users_schema.json")
    usernam = "Kamren"
    city = "Roscoeview"
    user_found = any(obj.get("username") == usernam and obj.get("address", {}).get("city") == city for obj in test_object.response_data)
    assert user_found
