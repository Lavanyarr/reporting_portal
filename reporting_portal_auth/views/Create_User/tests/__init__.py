# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal_auth"
OPERATION_NAME = "Create_User"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01CreateUserAPITestCase

__all__ = [
    "TestCase01CreateUserAPITestCase"
]
