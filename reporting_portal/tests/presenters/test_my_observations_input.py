from reporting_portal.presenters.get_observation_presenter_implementation \
    import GetObservationPresenterImplementation


class TestGetMyObservationsInput:

    def test_get_my_observations_when_invalid_limit_is_given(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_limit_response()


        # assert
        snapshot.assert_match(response.content, 'Invalid_limit_response')

    def test_get_my_observations_when_invalid_offset_is_given(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_offset_response()


        # assert
        snapshot.assert_match(response.content, 'Invalid_offset_response')

    def test_get_my_observations_when_invalid_sort_type_is_given(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_sort_type_response()


        # assert
        snapshot.assert_match(response.content, 'Invalid_sort_type_response')


    def test_get_my_observations_when_invalid_filter_type_is_given(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_filter_type_response()


        # assert
        snapshot.assert_match(response.content, 'Invalid_filter_type_response')

    def test_get_my_observations_when_invalid_sort_field_is_given(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        # act
        response = presenter.prepare_invalid_sort_field_response()


        # assert
        snapshot.assert_match(response.content, 'Invalid_sort_field_response')