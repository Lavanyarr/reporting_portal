
import abc
from typing import List

from reporting_portal.interactors.storages.dtos import (
    CategoryDTO,
    SubCategoryDTO, ObservationDTO
)


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_categories_of_observation(self)-> CategoryDTO:
        pass

    @abc.abstractmethod
    def get_subcategories(self, categories_ids: List[int])-> SubCategoryDTO:
        pass

    @abc.abstractmethod
    def validate_category_id(self, category_id: int):
        pass

    @abc.abstractmethod
    def validate_subcategory_id(self, category_id: int, subcategory_id: int):
        pass

    @abc.abstractmethod
    def create_observation(self, observation_dto:ObservationDTO):
        pass