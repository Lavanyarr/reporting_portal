import pytest

from reporting_portal.interactors.storages.dtos import ObservationDTO
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
        SubCategoryFactory.reset_sequence()
        CategoryFactory.create()
        SubCategoryFactory.create(category_id=1)
        observation_dto = ObservationDTO(
            title='deviations',
            category_id=1,
            subcategory_id=1,
            severity='HIGH',
            description='In learning hours',
            attachments=["photo"]
        )

        # act
        storage.create_observation(observation_dto)

