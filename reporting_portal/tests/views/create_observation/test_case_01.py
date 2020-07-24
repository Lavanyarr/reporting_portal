"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateObservationAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    # @pytest.fixture()
    # def setup(self, api_user):
    #     from reporting_portal.tests.factories.storage_factories \
    #         import CategoryFactory, SubCategoryFactory
    #     CategoryFactory.reset_sequence()
    #     CategoryFactory.create()
    #     SubCategoryFactory.reset_sequence()
    #     SubCategoryFactory.create(category_id=1)


    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'title': 'string',
            'category_id': 1,
            'sub_category_id': 1,
            'severity': 'HIGH',
            'description': 'string',
            'attachments': ['string']
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
