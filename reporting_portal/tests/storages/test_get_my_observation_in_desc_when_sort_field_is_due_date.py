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

    def test_get_observations_in_desc_when_sort_field_is_due_date(self, snapshot):
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
        response = storage.get_my_observation_in_dec_when_given_sort_field_is_due_date(observation_dto)

        # assert
        snapshot.assert_match(response, "observation_objs")
