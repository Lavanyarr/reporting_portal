import pytest

from reporting_portal.exceptions.exceptions import InvalidSubCategoryId
from reporting_portal.storages.storage_implementation \
    import StorageImplementation
from reporting_portal.tests.factories.storage_factories import (
    CategoryFactory,
    SubCategoryFactory
)


@pytest.mark.django_db
class TestCategoryId:

    def test_invalid_subcategory_id_of_category_for_observation(self):
        # arrange
        category_id = 1
        sub_category_id = 10
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(1)
        SubCategoryFactory.create(category_id=1)

        # act
        with pytest.raises(InvalidSubCategoryId):
            storage.validate_subcategory_id(category_id, sub_category_id)

    def test_valid_subcategory_id_of_category_for_observation(self):
        # arrange
        category_id = 1
        sub_category_id = 1
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(1)
        SubCategoryFactory.create(category_id=1)

        # act
        storage.validate_subcategory_id(category_id, sub_category_id)
