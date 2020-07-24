import datetime

import factory

from reporting_portal.interactors.storages.dtos import (
    CategoryDTO,
    SubCategoryDTO,
    ObservationDTO,
    ObservationDetailsDTO
)
from reporting_portal.constants.enums import (
    Severity,
    Status
)


class CategoryDTOFactory(factory.Factory):
    class Meta:
        model = CategoryDTO

    id = factory.sequence(lambda x: x + 1)
    name = factory.sequence(lambda x: "category_{0}".format(x + 1))


class SubCategoryDTOFactory(factory.Factory):
    class Meta:
        model = SubCategoryDTO

    category_id = factory.sequence(lambda x: x + 1)
    id = factory.sequence(lambda x: x + 1)
    name = factory.sequence(lambda x: "category_{0}".format(x + 1))


SEVERITY = Severity.get_list_of_tuples()
STATUS = Status.get_list_of_tuples()

class ObservationFactory(factory.Factory):
    class Meta:
        model = ObservationDTO

    title = factory.sequence(lambda x: "title_{0}".format(x + 1))
    category_id = factory.sequence(lambda x: x + 1)
    subcategory_id = factory.sequence(lambda x: x + 1)
    severity = factory.Iterator(SEVERITY, getter=lambda c: c[0])
    description = factory.sequence(lambda x: "description_{0}".format(x + 1))
    attachments = factory.sequence(lambda x: "attachment_{0}".format(x + 1))


class ObservationDetailsFactory(factory.Factory):

    class Meta:
        model = ObservationDetailsDTO

    title = factory.sequence(lambda x: "title_{0}".format(x+1))
    severity= factory.Iterator(SEVERITY, getter=lambda c: c[0])
    status = factory.Iterator(STATUS, getter=lambda c: c[0])
    due_date = factory.LazyFunction(datetime.datetime.now)
    messages_count = factory.sequence(lambda x: x+1)