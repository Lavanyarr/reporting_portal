"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "title": "string",
    "category_id": 1,
    "sub_category_id": 10,
    "severity": "HIGH",
    "description": "string",
    "attachments": [
        "string"
    ]
}
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


class TestCase02CreateObservationAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02CreateObservationAPITestCase, self).setupUser(
            username=username, password=password
    )


    def test_case(self):

        from reporting_portal.tests.factories.storage_factories \
            import CategoryFactory, SubCategoryFactory
        CategoryFactory.reset_sequence()
        CategoryFactory.create()
        SubCategoryFactory.reset_sequence()
        SubCategoryFactory.create(category_id=1)
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.