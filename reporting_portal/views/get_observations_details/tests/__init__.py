# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "get_observations_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_observation_details/v1/"

from .test_case_01 import TestCase01GetObservationsDetailsAPITestCase

__all__ = [
    "TestCase01GetObservationsDetailsAPITestCase"
]
