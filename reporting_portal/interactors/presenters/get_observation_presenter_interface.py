import abc

from reporting_portal.interactors.storages.dtos import UserObservationDTO


class GetObservationPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_invalid_observation_ids_response(self):
        pass

    @abc.abstractmethod
    def prepare_invalid_limit_response(self):
        pass

    @abc.abstractmethod
    def prepare_invalid_offset_response(self):
        pass

    @abc.abstractmethod
    def prepare_invalid_sort_type_response(self):
        pass

    @abc.abstractmethod
    def prepare_invalid_filter_type_response(self):
        pass

    @abc.abstractmethod
    def prepare_invalid_sort_field_response(self):
        pass

    @abc.abstractmethod
    def prepare_my_observation_list(self, user_total_observation_dto: UserObservationDTO):
        pass