import abc

from typing import List

from reporting_portal.interactors.storages.dtos import ObservationDetailsDTO


class ObservationStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_valid_observation_ids(self, observation_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_observation_details(self, valid_observation_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_my_observation_in_dec_when_given_sort_field_is_reported_on(
            self, observation_dto: ObservationDetailsDTO):
        pass

    @abc.abstractmethod
    def get_my_observation_in_dec_when_given_sort_field_is_due_date(
            self, observation_dto: ObservationDetailsDTO):
        pass

    @abc.abstractmethod
    def get_my_observation_when_given_sort_field_is_reported_on(
            self, observation_dto: ObservationDetailsDTO):
        pass

    @abc.abstractmethod
    def get_my_observation_when_given_sort_field_is_due_date(
            self, observation_dto: ObservationDetailsDTO):
        pass
