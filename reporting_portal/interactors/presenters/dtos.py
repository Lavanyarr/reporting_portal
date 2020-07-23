
import dataclasses

from reporting_portal.interactors.storages.dtos import CategoryDTO, SubCategoryDTO


@dataclasses.dataclass()
class CategoryWithSubCategoryDTO:
    category_dto: CategoryDTO
    subcategory_dto: SubCategoryDTO
