# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "get_my_observations"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_observations/v1/"

from .test_case_01 import TestCase01GetMyObservationsAPITestCase

__all__ = [
    "TestCase01GetMyObservationsAPITestCase"
]
