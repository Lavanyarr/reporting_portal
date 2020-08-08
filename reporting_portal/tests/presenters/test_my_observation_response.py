from reporting_portal.interactors.storages.dtos import UserObservationDTO
from reporting_portal.presenters.get_observation_presenter_implementation \
    import GetObservationPresenterImplementation
from reporting_portal.tests.factories.dto_factories import (
    ObservationDetailsFactory,
    UserDtoFactory, ObservationDetailsWithCountFactory
)


class TestMyObservations:
    def test_get_observations_list_response(self, snapshot):
        # arrange
        presenter = GetObservationPresenterImplementation()

        observation = ObservationDetailsWithCountFactory.create()
        user_details_Dto = UserDtoFactory.create_batch(1)
        user_total_observation_dto = UserObservationDTO(
            common_dto=observation,
            assigned_to=user_details_Dto
        )

        # act
        response = presenter.prepare_my_observation_list(user_total_observation_dto)

        # assert
        snapshot.assert_match(response.content, 'Invalid_sort_field_response')
