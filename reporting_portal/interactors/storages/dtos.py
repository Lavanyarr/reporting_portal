import dataclasses

from typing import List

from reporting_portal.constants.enums import SEVERITY


@dataclasses.dataclass()
class CategoryDTO:
    id: int
    name: str


@dataclasses.dataclass()
class SubCategoryDTO:
    category_id: int
    id: int
    name: str


@dataclasses.dataclass()
class CategoryWithSubCategoryDTO:
    category_dto: CategoryDTO
    subcategory_dto: SubCategoryDTO


severity = SEVERITY.get_list_of_tuples()


@dataclasses.dataclass()
class ObservationDTO:
    title: str
    category_id: int
    subcategory_id: int
    severity: severity
    description: str
    attachments: List[str]
