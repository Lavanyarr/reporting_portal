import dataclasses
import datetime

from typing import List

from reporting_portal.constants.enums import (
    Severity,
    Status,
    Sort,
    SortField
)


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


SEVERITY = Severity.get_list_of_tuples()
STATUS = Status.get_list_of_tuples()


@dataclasses.dataclass()
class ObservationDTO:
    title: str
    category_id: int
    subcategory_id: int
    severity: SEVERITY
    description: str
    attachments: List[str]


@dataclasses.dataclass()
class ObservationDetailsDTO:
    title: str
    severity: SEVERITY
    status: STATUS
    due_date: datetime
    messages_count: int


SORT = Sort.get_list_of_tuples()
SORTFIELD = Sort.get_list_of_tuples()


@dataclasses.dataclass()
class ObservationInputDTO:
    limit: str
    offset: str
    sort_type: SORT
    filter_type: STATUS
    sort_field: SORTFIELD
