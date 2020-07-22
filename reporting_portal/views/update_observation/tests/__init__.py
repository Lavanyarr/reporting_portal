# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "update_observation"
REQUEST_METHOD = "put"
URL_SUFFIX = "update_observation/v1/"

from .test_case_01 import TestCase01UpdateObservationAPITestCase

__all__ = [
    "TestCase01UpdateObservationAPITestCase"
]
