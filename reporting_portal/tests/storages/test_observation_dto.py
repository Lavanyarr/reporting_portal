import pytest

from reporting_portal.storages.observation_storage_implementation import \
    ObservationStorageImplementation


from reporting_portal.tests.factories.storage_factories \
    import ObservationDetailsFactory


@pytest.mark.django_db
class TestGetValidObservationIds:

    def test_when_valid_observation_ids_are_given(self, snapshot):
        # arrange
        observation_ids = [1, 2]
        storage = ObservationStorageImplementation()
        ObservationDetailsFactory.reset_sequence()
        ObservationDetailsFactory.create_batch(2)

        # act
        response = storage.get_observation_details(observation_ids)

        # assert
        snapshot.assert_match(response, 'response')
