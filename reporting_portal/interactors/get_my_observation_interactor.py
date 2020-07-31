from reporting_portal.exceptions.exceptions import (
    InvalidOffset,
    InvalidLimit, InvalidSortType, InvalidFilterType,
    InvalidSortField
)
from reporting_portal.interactors.storages.dtos import ObservationInputDTO
from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface
from reporting_portal.interactors.presenters.get_observation_presenter_interface \
    import GetObservationPresenterInterface

from reporting_portal.interactors.mixins import ValidationMixin


class GetMyObservationInteractor(ValidationMixin):

    def __init__(self, observation_storage: ObservationStorageInterface):
        self.storage = observation_storage

    def get_my_observation_wrapper(self, observation_dto: ObservationInputDTO,
                                   observation_presenter: GetObservationPresenterInterface):

        try:
            response = self.get_my_observation(observation_dto)
        except InvalidLimit:
            response = observation_presenter.prepare_invalid_limit_response()
        except InvalidOffset:
            response = observation_presenter.prepare_invalid_offset_response()
        except InvalidSortType:
            response = observation_presenter.prepare_invalid_sort_type_response()
        except InvalidFilterType:
            response = observation_presenter.prepare_invalid_filter_type_response()
        except InvalidSortField:
            response = observation_presenter.prepare_invalid_sort_field_response()
        return response

    def get_my_observation(self, observation_dto):

        self.validate_the_observation_details(observation_dto)
        observation_objs = self.get_observation_ids_of_observation(observation_dto)
        observation_ids = [
            observation.id
            for observation in observation_objs
        ]

        from reporting_portal.interactors.get_observation_details_dto \
            import GetObservationDTOInteractor
        observation_interactor = GetObservationDTOInteractor(
            observation_storage=self.storage
        )
        observation_dto = observation_interactor.get_observation_details_dto(observation_ids)

        return observation_dto
