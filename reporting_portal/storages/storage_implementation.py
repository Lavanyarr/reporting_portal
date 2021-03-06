from typing import List

from reporting_portal.exceptions.exceptions import (
    InvalidCategoryId,
    InvalidSubCategoryId
)
from reporting_portal.interactors.storages.storage_interface import StorageInterface
from reporting_portal.interactors.storages.dtos import (
    CategoryDTO,
    SubCategoryDTO, ObservationDTO
)
from reporting_portal.models import (
    Category,
    SubCategory,
    Observation,
    Attachments
)


class StorageImplementation(StorageInterface):

    def get_categories_of_observation(self) -> CategoryDTO:
        categories_obj = Category.objects.all()
        category_dto_list = self.convert_category_objects_to_dto(categories_obj)
        return category_dto_list

    @staticmethod
    def convert_category_objects_to_dto(categories):
        category_dto_list = []
        for category in categories:
            category_dto = CategoryDTO(
                id=category.id,
                name=category.name
            )
            category_dto_list.append(category_dto)
        return category_dto_list

    def get_subcategories(self, categories_ids: List[int]) -> SubCategoryDTO:
        subcategories_obj = SubCategory.objects.filter(category__in=categories_ids)
        subcategories_dto = self.convert_subcategory_objects_to_dto(subcategories_obj)
        return subcategories_dto

    @staticmethod
    def convert_subcategory_objects_to_dto(subcategories_obj):
        subcategories_list = []
        for subcategory in subcategories_obj:
            subcategory_dto = SubCategoryDTO(
                category_id=subcategory.category.id,
                id=subcategory.id,
                name=subcategory.name
            )
            subcategories_list.append(subcategory_dto)
        return subcategories_list

    def validate_category_id(self, category_id: int):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise InvalidCategoryId

    def validate_subcategory_id(self, category_id: int, subcategory_id: int):
        try:
            SubCategory.objects.get(id=subcategory_id,
                                    category_id=category_id)
        except SubCategory.DoesNotExist:
            raise InvalidSubCategoryId

    def create_observation(self, observation_dto: ObservationDTO):

        if observation_dto.category_id and observation_dto.subcategory_id:
            rp = SubCategory.objects.filter(
                id=observation_dto.category_id,
                category=observation_dto.category_id).values_list('rp', flat=True)
            assigned_rp = rp[0]
        else:
            assigned_rp = "Rp Not Assigned"

        observation_obj = Observation.objects.create(title=observation_dto.title,
                                                     description=observation_dto.description,
                                                     category_id=observation_dto.category_id,
                                                     subcategory_id=observation_dto.subcategory_id,
                                                     severity=observation_dto.severity,
                                                     assigned_to=assigned_rp)

        if observation_dto.attachments:

            for attachments in observation_dto.attachments:
                Attachments.objects.create(name=attachments, observation_id=observation_obj.id)
