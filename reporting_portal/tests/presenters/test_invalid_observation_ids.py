from reporting_portal.presenters.get_observation_presenter_implementation \
    import GetObservationPresenterImplementation


class TestInvalidObservationIds:

    def test_get_observations_with_invalid_observation_ids(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_observation_ids_response()

        # assert
        snapshot.assert_match(response.content, 'Invalid_observation_ids')
