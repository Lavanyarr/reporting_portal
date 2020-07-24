from datetime import datetime

import factory

from reporting_portal.models import (
    Category,
    SubCategory,
    Observation
)
from reporting_portal.constants.enums import (
    Severity,
    Status
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.sequence(lambda x: "category_{0}".format(x + 1))


class SubCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubCategory

    name = factory.sequence(lambda x: "sub_category_{0}".format(x + 1))
    category = factory.SubFactory(CategoryFactory)
    rp = factory.sequence(lambda x: x + 1)


SEVERITY = Severity.get_list_of_tuples()
STATUS = Status.get_list_of_tuples()


class ObservationDetailsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Observation

    title = factory.sequence(lambda x: "title_{0}".format(x + 1))
    category = factory.SubFactory(CategoryFactory)
    subcategory = factory.SubFactory(SubCategoryFactory)
    severity = factory.Iterator(SEVERITY, getter=lambda c: c[0])
    status = factory.Iterator(STATUS, getter=lambda c: c[0])
    assigned_to = factory.sequence(lambda x: x + 1)
    reported_on = factory.LazyFunction(datetime.now)
    due_date = factory.LazyFunction(datetime.now)
    reported_by = factory.sequence(lambda x: x + 1)
