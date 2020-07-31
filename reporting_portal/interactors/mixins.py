from reporting_portal.exceptions.exceptions import (
    InvalidLimit,
    InvalidOffset,
    InvalidSortType,
    InvalidFilterType,
    InvalidSortField
)
from reporting_portal.interactors.storages.dtos import ObservationInputDTO


class ValidationMixin:

    def validate_the_observation_details(self, observation_dto: ObservationInputDTO):

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

    def get_observation_ids_of_observation(self, observation_dto):

        if observation_dto.sort_type == 'DESC' and observation_dto.sort_field == 'REPORTED_ON':
            observation_objs = self.storage.get_my_observation_in_dec_when_given_sort_field_is_reported_on(
                observation_dto)
        elif observation_dto.sort_type == 'DESC' and observation_dto.sort_field == 'DUE_DATE':
            observation_objs = self.storage.get_my_observation_in_dec_when_given_sort_field_is_due_date(observation_dto)
        elif observation_dto.sort_field == 'REPORTED_ON':
            observation_objs = self.storage.get_my_observation_when_given_sort_field_is_reported_on(observation_dto)
        elif observation_dto.sort_field == 'DUE_DATE':
            observation_objs = self.storage.get_my_observation_when_given_sort_field_is_due_date(observation_dto)
        return observation_objs

    @staticmethod
    def check_given_value_is_negative(value):
        if value < 0:
            return True
        return False

    @staticmethod
    def check_sort_type_is_valid(sort_type):
        valid_sort_type = ["ASC", "DESC"]
        if sort_type not in valid_sort_type:
            return True
        return False

    @staticmethod
    def check_filter_type_is_valid(filter_type):
        valid_filter_type = ["ALL",
                             "ACTION_IN_PROGRESS",
                             "ACKNOWLEDGED_BY_RP",
                             "RESOLVED",
                             "CLOSED",
                             "REPORTED"]
        if filter_type not in valid_filter_type:
            return True
        return False

    @staticmethod
    def check_sort_field_is_valid(sort_field):
        valid_filter_type = ["DUE_DATE", "REPORTED_ON"]
        if sort_field not in valid_filter_type:
            return True
        return False
