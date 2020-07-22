"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from reporting_portal.tests.factories.storage_factories import (
    CategoryFactory,
    SubCategoryFactory
)
REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetCategoriesWithSubcategoriesAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetCategoriesWithSubcategoriesAPITestCase,self).setupUser(
            username=username, password=password)

    def test_case(self):
        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(2)
        SubCategoryFactory.reset_sequence()
        SubCategoryFactory.create_batch(2, category=category[0])
        self.default_test_case() # Returns response object.
