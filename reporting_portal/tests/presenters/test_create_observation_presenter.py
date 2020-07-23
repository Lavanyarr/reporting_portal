
import json
from reporting_portal.presenters.observation_presenter_implementation \
    import ObservationPresenterImplementation

class TestCreateObservation:

    def test_invalid_category_id_for_observation(self, snapshot):

        #arrange
        presenter = ObservationPresenterImplementation()

        #act
        response = presenter.raise_invalid_category_id_exception()

        #assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'invalid_category_id')

    def test_invalid_sub_category_id_for_observation(self, snapshot):

        #arrange
        presenter = ObservationPresenterImplementation()

        #act
        response = presenter.raise_invalid_subcategory_id_for_category_exception()

        #assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'invalid_category_id')

    def test_create_observation_with_valid_details(self, snapshot):
        # arrange
        presenter = ObservationPresenterImplementation()

        # act
        response = presenter.get_create_observation_response()

        # assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'invalid_category_id')