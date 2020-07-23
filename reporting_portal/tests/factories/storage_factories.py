import factory

from reporting_portal.models import (
    Category,
    SubCategory
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
    rp = factory.sequence(lambda x: x+1)


