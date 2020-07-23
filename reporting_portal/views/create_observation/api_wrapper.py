from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import dataclasses
from typing import List

from reporting_portal.storages.storage_implementation \
    import StorageImplementation
from reporting_portal.presenters.observation_presenter_implementation \
    import ObservationPresenterImplementation
from reporting_portal.constants.enums import Severity
from ...interactors.create_observation_interactor import CreateObservationInteractor

SEVERITY = Severity.get_list_of_tuples()


@dataclasses.dataclass()
class ObservationDto:
    title: str
    category_id: int
    subcategory_id: int
    severity: SEVERITY
    description: str
    attachments: List[str]


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    title = request_data['title']
    category_id = request_data['category_id']
    sub_category_id = request_data['sub_category_id']
    severity = request_data['severity']
    description = request_data['description']
    attachments = request_data['attachments']

    observation_dto = ObservationDto(
        title=title,
        category_id=category_id,
        subcategory_id=sub_category_id,
        severity=severity,
        description=description,
        attachments=attachments
    )

    storage = StorageImplementation()
    presenter = ObservationPresenterImplementation()

    interactor = CreateObservationInteractor(
        storage=storage
    )
    response = interactor.create_observation_wrapper(
        observation_dto=observation_dto,
        presenter=presenter
    )
    return response
