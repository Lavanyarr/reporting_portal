import pytest

from reporting_portal.interactors.storages.dtos import ObservationInputDTO
from reporting_portal.storages.observation_storage_implementation \
    import ObservationStorageImplementation

from reporting_portal.tests.factories.storage_factories \
    import ObservationDetailsFactory
from reporting_portal.constants.enums import (
    Sort,
    Status,
    SortField
)


@pytest.mark.django_db
class TestObservation:

    def test_get_observations_when_sort_field_is_reported_by(self, snapshot):
        # arrange
        storage = ObservationStorageImplementation()
        ObservationDetailsFactory.reset_sequence(1)
        ObservationDetailsFactory.create_batch(5, status='REPORTED', severity='WARNING')
        observation_dto = ObservationInputDTO(
            limit=1,
            offset=3,
            sort_type=Sort.DESC.value,
            filter_type=Status.REPORTED.value,
            sort_field=SortField.DUE_DATE.value
        )

        # act
        response = storage.get_my_observation_when_given_sort_field_is_reported_on(observation_dto)

        # assert
        snapshot.assert_match(response, "observation_objs")
