from reporting_portal.exceptions.exceptions import (
    InvalidOffset,
    InvalidLimit, InvalidSortType, InvalidFilterType,
    InvalidSortField
)
from reporting_portal.interactors.storages.dtos import ObservationInputDTO, UserObservationDTO
from reporting_portal.interactors.storages.observation_storage_interface \
    import ObservationStorageInterface
from reporting_portal.interactors.presenters.get_observation_presenter_interface \
    import GetObservationPresenterInterface
from reporting_portal.adapters.service_adapter import get_service_adapter
from reporting_portal.interactors.mixins import ValidationMixin


class GetMyObservationInteractor(ValidationMixin):

    def __init__(self, observation_storage: ObservationStorageInterface):
        self.storage = observation_storage

    def get_my_observation_wrapper(self, observation_dto: ObservationInputDTO,
                                   observation_presenter: GetObservationPresenterInterface):

        try:
            user_total_observation_dto = self.get_my_observation(observation_dto)
            response = observation_presenter.prepare_my_observation_list(user_total_observation_dto)
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

        user_ids = [
            user.assigned_to
            for user in observation_objs if user.assigned_to != "Rp Not Assigned"
        ]
        observation_ids = [
            observation.id
            for observation in observation_objs
        ]

        from reporting_portal.interactors.get_observation_details_dto \
            import GetObservationDTOInteractor
        observation_interactor = GetObservationDTOInteractor(
            observation_storage=self.storage
        )
        common_observation_dto = observation_interactor.get_observation_details_dto(observation_ids)
        service = get_service_adapter()
        user_dto = service.auth_service.get_user_dtos(user_ids=user_ids)

        user_total_observation_dto = UserObservationDTO(
            common_dto=common_observation_dto,
            assigned_to=user_dto
        )

        return user_total_observation_dto
