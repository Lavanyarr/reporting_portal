import abc
from reporting_portal.interactors.storages.dtos import (
    CategoryWithSubCategoryDTO
)


class CategoriesPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_categories_with_subacategories_response(self, response_dto: CategoryWithSubCategoryDTO):
        pass
