import pytest
from reporting_portal.storages.storage_implementation import StorageImplementation
from reporting_portal.tests.factories.storage_factories import (
    CategoryFactory,
    SubCategoryFactory
)

@pytest.mark.django_db
class TestGetCategories:

    def test_subcategories_when_category_as_no_subcategories(self, snapshot):
        # arrange
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        CategoryFactory.create_batch(2)
        category_ids = [1,2]

        # act
        response = storage.get_subcategories(category_ids)

        # assert
        snapshot.assert_match(response, 'subcategory_dto')

    def test_subcategories_when_category_have_subcategories(self, snapshot):
        # arrange
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(2)
        SubCategoryFactory.reset_sequence()
        SubCategoryFactory.create_batch(2,category=category[0])
        category_ids = [1,2]

        # act
        response = storage.get_subcategories(category_ids)

        # assert
        snapshot.assert_match(response, 'subcategory_dto')

