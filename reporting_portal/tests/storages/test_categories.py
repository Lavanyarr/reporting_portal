'''

TODO:
     test categories;
         no catgories
         categories present form dto
'''

import pytest
from reporting_portal.storages.storage_implementation import StorageImplementation
from reporting_portal.tests.factories.storage_factories import CategoryFactory

@pytest.mark.django_db
class TestGetCategories:

    def test_get_categories_when_there_are_no_categories(self, snapshot):
        # arrange
        storage = StorageImplementation()

        # act
        response = storage.get_categories_of_observation()

        # assert
        snapshot.assert_match(response, 'category_dto')

    def test_get_categories_when_there_are_categories(self, snapshot):
        # arrange
        storage = StorageImplementation()

        CategoryFactory.reset_sequence()
        CategoryFactory.create_batch(3)
        # act
        response = storage.get_categories_of_observation()

        # assert
        snapshot.assert_match(response, 'category_dto')