# pylint: disable=wrong-import-position

APP_NAME = "reporting_portal"
OPERATION_NAME = "Get_categories_with_subcategories"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_categories_with_subcategories/v1/"

from .test_case_01 import TestCase01GetCategoriesWithSubcategoriesAPITestCase

__all__ = [
    "TestCase01GetCategoriesWithSubcategoriesAPITestCase"
]
