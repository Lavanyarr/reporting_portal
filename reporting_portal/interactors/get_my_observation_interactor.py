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





class GetMyObservationInteractor:

    def __init__(self, observation_storage:ObservationStorageInterface ):
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

    def get_my_observation(self, observation_dto: ObservationInputDTO):

        is_negative = self.check_given_value_is_negative(observation_dto.limit)
        if is_negative:
            raise InvalidLimit

        is_negative = self.check_given_value_is_negative(observation_dto.offset)
        if is_negative:
            raise InvalidOffset

        is_valid = self.check_sort_type_is_valid(observation_dto.sort_type)
        if is_valid:
            raise InvalidSortType

        is_valid = self.check_filter_type_is_valid(observation_dto.filter_type)
        if is_valid:
            raise InvalidFilterType

        is_valid = self.check_sort_field_is_valid(observation_dto.sort_field)
        if is_valid:
            raise InvalidSortField

    @staticmethod
    def check_given_value_is_negative(value):
        if value < 0:
            return True
        return False

    @staticmethod
    def check_sort_type_is_valid(sort_type):
        valid_sort_type = ["ASC","DESC"]
        if sort_type not in valid_sort_type:
            return True
        return False

    @staticmethod
    def check_filter_type_is_valid(filter_type):
        valid_filter_type = ["ALL",
                             "ACTION_IN_PROGRESS",
                             "ACKNOWLEDGE_BY",
                             "RESOLVED",
                             "CLOSED"]
        if filter_type not in valid_filter_type:
            return True
        return False

    @staticmethod
    def check_sort_field_is_valid(sort_field):
        valid_filter_type = ["DUE_DATE","REPORTED_ON"]
        if sort_field not in valid_filter_type:
            return True
        return False
