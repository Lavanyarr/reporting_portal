from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from reporting_portal.storages.observation_storage_implementation \
    import ObservationStorageImplementation
from reporting_portal.presenters.get_observation_presenter_implementation \
    import GetObservationPresenterImplementation
from ...interactors.get_my_observation_interactor import GetMyObservationInteractor
from ...interactors.storages.dtos import ObservationInputDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_params = kwargs['request_query_params']
    limit = request_params['limit']
    offset = request_params['offset']
    request_data = kwargs['request_data']
    sort_type = request_data['sort_type']
    filter_type = request_data['filter_type']
    sort_field = request_data['sort_field']

    observation_dto = ObservationInputDTO(
        limit=limit,
        offset=offset,
        sort_type=sort_type,
        filter_type=filter_type,
        sort_field=sort_field

    )
    storage = ObservationStorageImplementation()
    presenter = GetObservationPresenterImplementation()

    interactor = GetMyObservationInteractor(
        observation_storage=storage
    )
    response = interactor.get_my_observation_wrapper(
        observation_dto=observation_dto,
        observation_presenter=presenter
    )
    return response

# @validate_decorator(validator_class=ValidatorClass)
# def api_wrapper(*args, **kwargs):
#     # ---------MOCK IMPLEMENTATION---------
#     try:
#         from reporting_portal.views.get_my_observations.tests.test_case_01 \
#             import TEST_CASE as test_case
#     except ImportError:
#         from reporting_portal.views.get_my_observations.tests.test_case_01 \
#             import test_case
#
#     from django_swagger_utils.drf_server.utils.server_gen.mock_response \
#         import mock_response
#     try:
#         from reporting_portal.views.get_my_observations.request_response_mocks \
#             import RESPONSE_200_JSON
#     except ImportError:
#         RESPONSE_200_JSON = ''
#     response_tuple = mock_response(
#         app_name="reporting_portal", test_case=test_case,
#         operation_name="get_my_observations",
#         kwargs=kwargs, default_response_body=RESPONSE_200_JSON)
#     return response_tuple[1]
