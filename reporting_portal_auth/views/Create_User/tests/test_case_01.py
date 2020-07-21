"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "username": "lavanya",
    "password": "lavanya1"
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

from unittest.mock import patch
import datetime
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

from reporting_portal_auth.tests.storages.dtos import UserAuthTokensDTO
user_token_dto = UserAuthTokensDTO(user_id=1,
                                           access_token='XpCbV4bTl6v43HTsexE1SUxoNiO7qG',
                                           refresh_token='amNMDAKB1hMgMpHzjxr6rzHTz59SJo',
                                           expires_in=datetime.datetime(5189, 4, 11, 20, 55, 5, 722643)
                                           )
from reporting_portal_auth.tests.factories.storage_dtos import UserFactory
class TestCase01CreateUserAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    @patch.object(OAuthUserAuthTokensService,'create_user_auth_tokens', return_value=user_token_dto)
    def test_case(self, auth_service):
        UserFactory.reset_sequence()
        user = UserFactory.create(username="lavanya", password='lavanya1')
        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
