# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "create_observation"
REQUEST_METHOD = "post"
URL_SUFFIX = "create_observation/v1/"

from .test_case_01 import TestCase01CreateObservationAPITestCase

__all__ = [
    "TestCase01CreateObservationAPITestCase"
]
