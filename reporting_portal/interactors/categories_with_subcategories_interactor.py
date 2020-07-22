import dataclasses
from reporting_portal.interactors.storages.storage_interface \
    import StorageInterface
from reporting_portal.interactors.presenters.categories_presenter_interface \
    import CategoriesPresenterInterface
from reporting_portal.interactors.storages.dtos import (
    CategoryWithSubCategoryDTO
)


class CategoriesWithSubCategoriesInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_categories_with_subcategories_wrapper(self,
                                                  presenter: CategoriesPresenterInterface):
        response_dto = self.get_categories_with_subcategories()
        return presenter.get_categories_with_subacategories_response(response_dto)

    def get_categories_with_subcategories(self):
        categories_ids = []
        categories_dto = self.storage.get_categories_of_observation()

        if categories_dto:
            categories_ids = [category.id for category in categories_dto]

        subcategories_dto = self.storage.get_subcategories(categories_ids)

        category_with_subcategory_dto = CategoryWithSubCategoryDTO(
            category_dto= categories_dto,
            subcategory_dto= subcategories_dto
        )
        return category_with_subcategory_dto
