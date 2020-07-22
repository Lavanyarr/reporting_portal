"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "useer",
    "password": "user"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}

from reporting_portal_auth.tests.factories.storage_dtos import UserFactory


class TestCase02CreateUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        UserFactory.reset_sequence()
        user = UserFactory(username="lavanya", password='lavanya1')
        user.set_password('lavanya1')
        user.save()

        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
