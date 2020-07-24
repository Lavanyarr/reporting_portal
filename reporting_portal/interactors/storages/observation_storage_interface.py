import abc

from typing import List


class ObservationStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_valid_observation_ids(self, observation_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_observation_details(self, valid_observation_ids: List[int]):
        pass