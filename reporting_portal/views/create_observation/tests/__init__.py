# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "create_observation"
REQUEST_METHOD = "post"
URL_SUFFIX = "create_observation/v1/"

from .test_case_01 import TestCase01CreateObservationAPITestCase
from .test_case_02 import TestCase02CreateObservationAPITestCase
from .test_case_03 import TestCase03CreateObservationAPITestCase

__all__ = [
    "TestCase01CreateObservationAPITestCase",
    "TestCase02CreateObservationAPITestCase",
    "TestCase03CreateObservationAPITestCase"
]
