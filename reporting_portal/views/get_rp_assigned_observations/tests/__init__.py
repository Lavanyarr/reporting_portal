# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "get_rp_assigned_observations"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_observations_of_rp/v1/"

from .test_case_01 import TestCase01GetRpAssignedObservationsAPITestCase

__all__ = [
    "TestCase01GetRpAssignedObservationsAPITestCase"
]
