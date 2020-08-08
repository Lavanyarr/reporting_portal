import datetime

import pytest
from freezegun import freeze_time

from reporting_portal.storages.observation_storage_implementation import \
    ObservationStorageImplementation


from reporting_portal.tests.factories.storage_factories \
    import ObservationDetailsFactory


@pytest.mark.django_db
@freeze_time("2012-01-14 00:00:00")
class TestGetValidObservationIds:

    def test_when_valid_observation_ids_are_given(self, snapshot):
        # arrange
        observation_ids = [1, 2]
        storage = ObservationStorageImplementation()
        ObservationDetailsFactory.reset_sequence()
        ObservationDetailsFactory.create_batch(
            2, due_date=datetime.datetime(2020, 7, 31, 16, 5, 54, 365804), status='RESOLVED', severity='WARNING',
            reported_on=datetime.datetime(2020, 7, 5, 16, 5, 54, 365803)
        )

        # act
        response = storage.get_observation_details(observation_ids)

        # assert
        snapshot.assert_match(response, 'response')
