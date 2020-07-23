import pytest

from reporting_portal.exceptions.exceptions import InvalidCategoryId
from reporting_portal.storages.storage_implementation \
    import StorageImplementation
from reporting_portal.tests.factories.storage_factories import CategoryFactory


@pytest.mark.django_db
class TestCategoryId:

    def test_invalid_category_id_of_observation(self):
        # arrange
        category_id = 10
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        CategoryFactory.create()

        # act
        with pytest.raises(InvalidCategoryId):
            storage.validate_category_id(category_id)

    def test_valid_category_id_of_observation(self):
        # arrange
        category_id = 1
        storage = StorageImplementation()
        CategoryFactory.reset_sequence()
        CategoryFactory.create()

        # act
        storage.validate_category_id(category_id)
