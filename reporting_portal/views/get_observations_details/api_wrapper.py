from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    try:
        from reporting_portal.views.get_observations_details.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from reporting_portal.views.get_observations_details.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from reporting_portal.views.get_observations_details.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="reporting_portal", test_case=test_case,
        operation_name="get_observations_details",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON)
    return response_tuple[1]