'''
observation_ids:

dto: title
    due_date
    severity
    status
    message_count
    2. get valid observation ids

    1. invalid observation ids
    2 valid observation ids
'''

import pytest
from unittest.mock import create_autospec

from reporting_portal.exceptions.exceptions import InvalidObservationIds
from reporting_portal.interactors.get_observation_details_dto import GetObservationDTOInteractor
from reporting_portal.tests.factories.dto_factories import ObservationDetailsFactory, ObservationDetailsWithCountFactory


class TestGetObservationDTO:

    @pytest.fixture()
    def storage_mock(self):
        from reporting_portal.interactors.storages.observation_storage_interface \
            import ObservationStorageInterface
        storage = create_autospec(ObservationStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from reporting_portal.interactors.presenters.get_observation_presenter_interface \
            import GetObservationPresenterInterface

        presenter = create_autospec(GetObservationPresenterInterface)
        return presenter

    def test_observation_dto_with_invalid_observation_ids(self,
                                                          storage_mock,
                                                          presenter_mock):
        # arrange
        invalid_observation_ids = [3, 4]
        valid_observation_ids = [3]

        interactor = GetObservationDTOInteractor(
            observation_storage=storage_mock
        )
        storage_mock.get_valid_observation_ids.return_value = valid_observation_ids
        invalid_observation_ids_exception = InvalidObservationIds
        presenter_mock.prepare_invalid_observation_ids_response.return_value = InvalidObservationIds

        # act
        response = interactor.get_observation_details_dto_wrapper(
            invalid_observation_ids,
            observation_presenter=presenter_mock
        )

        # assert
        storage_mock.get_valid_observation_ids.assert_called_once()
        presenter_mock.prepare_invalid_observation_ids_response.call_args
        assert response == invalid_observation_ids_exception

    def test_observation_dto_with_valid_observation_ids(self,
                                                          storage_mock,
                                                          presenter_mock):
        # arrange
        observation_ids = [1,2]
        valid_observation_ids = [1, 2]

        interactor = GetObservationDTOInteractor(
            observation_storage=storage_mock
        )
        storage_mock.get_valid_observation_ids.return_value = valid_observation_ids
        observation_dto = ObservationDetailsWithCountFactory.create_batch(2)
        storage_mock.get_observation_details.return_value=observation_dto
        # act
        response = interactor.get_observation_details_dto_wrapper(
            observation_ids,
            observation_presenter=presenter_mock
        )

        # assert
        storage_mock.get_valid_observation_ids.assert_called_once()
        storage_mock.get_observation_details.assert_called_once_with(observation_ids)
        assert response == observation_dto

