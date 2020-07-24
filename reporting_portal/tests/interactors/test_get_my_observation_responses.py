'''
TODO:

invalid cases: offset negative value
                limit negative value
                check sort type
                check filter type
                check sort field

'''

from unittest.mock import (
    create_autospec,
    Mock
)
import pytest

from reporting_portal.interactors.storages.dtos import ObservationInputDTO


class TestGetMyObservations:

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

    def test_get_my_observation_when_limit_is_invalid(self, storage_mock, presenter_mock):
        # arrange
        from reporting_portal.interactors.get_my_observation_interactor \
            import GetMyObservationInteractor

        interactor = GetMyObservationInteractor(
            observation_storage=storage_mock
        )
        observation_dto = ObservationInputDTO(
            limit=-1,
            offset=10,
            sort_type="ASC",
            filter_type="ALL",
            sort_field="REPORTED_ON"
        )
        invalid_limit_obj = Mock()
        presenter_mock.prepare_invalid_limit_response.return_value = invalid_limit_obj

        # act
        response = interactor.get_my_observation_wrapper(
            observation_dto=observation_dto,
            observation_presenter=presenter_mock
        )

        # assert
        presenter_mock.prepare_invalid_limit_response.assert_called_once()
        assert response == invalid_limit_obj

    def test_get_my_observation_when_offset_is_invalid(self, storage_mock, presenter_mock):
        # arrange
        from reporting_portal.interactors.get_my_observation_interactor \
            import GetMyObservationInteractor

        interactor = GetMyObservationInteractor(
            observation_storage=storage_mock
        )
        observation_dto = ObservationInputDTO(
            limit=1,
            offset=-1,
            sort_type="ASC",
            filter_type="ALL",
            sort_field="REPORTED_ON"
        )
        invalid_offset_obj = Mock()
        presenter_mock.prepare_invalid_offset_response.return_value = invalid_offset_obj

        # act
        response = interactor.get_my_observation_wrapper(
            observation_dto=observation_dto,
            observation_presenter=presenter_mock
        )

        # assert
        presenter_mock.prepare_invalid_offset_response.assert_called_once()
        assert response == invalid_offset_obj

    def test_get_my_observation_when_sort_type_is_invalid(self, storage_mock, presenter_mock):
        # arrange
        from reporting_portal.interactors.get_my_observation_interactor \
            import GetMyObservationInteractor

        interactor = GetMyObservationInteractor(
            observation_storage=storage_mock
        )
        observation_dto = ObservationInputDTO(
            limit=1,
            offset=1,
            sort_type="A",
            filter_type="ALL",
            sort_field="REPORTED_ON"
        )
        invalid_sort_type = Mock()
        presenter_mock.prepare_invalid_sort_type_response.return_value = invalid_sort_type

        # act
        response = interactor.get_my_observation_wrapper(
            observation_dto=observation_dto,
            observation_presenter=presenter_mock
        )

        # assert
        presenter_mock.prepare_invalid_sort_type_response.assert_called_once()
        assert response == invalid_sort_type

    def test_get_my_observation_when_filter_type_is_invalid(self, storage_mock, presenter_mock):
        # arrange
        from reporting_portal.interactors.get_my_observation_interactor \
            import GetMyObservationInteractor

        interactor = GetMyObservationInteractor(
            observation_storage=storage_mock
        )
        observation_dto = ObservationInputDTO(
            limit=1,
            offset=1,
            sort_type="ASC",
            filter_type="A",
            sort_field="REPORTED_ON"
        )
        invalid_filter_type = Mock()
        presenter_mock.prepare_invalid_filter_type_response.return_value = invalid_filter_type

        # act
        response = interactor.get_my_observation_wrapper(
            observation_dto=observation_dto,
            observation_presenter=presenter_mock
        )

        # assert
        presenter_mock.prepare_invalid_filter_type_response.assert_called_once()
        assert response == invalid_filter_type

    def test_get_my_observation_when_sort_field_is_invalid(self, storage_mock, presenter_mock):
        # arrange
        from reporting_portal.interactors.get_my_observation_interactor \
            import GetMyObservationInteractor

        interactor = GetMyObservationInteractor(
            observation_storage=storage_mock
        )
        observation_dto = ObservationInputDTO(
            limit=1,
            offset=1,
            sort_type="ASC",
            filter_type="ALL",
            sort_field="R"
        )
        invalid_sort_field = Mock()
        presenter_mock.prepare_invalid_sort_field_response.return_value = invalid_sort_field

        # act
        response = interactor.get_my_observation_wrapper(
            observation_dto=observation_dto,
            observation_presenter=presenter_mock
        )

        # assert
        presenter_mock.prepare_invalid_sort_field_response.assert_called_once()
        assert response == invalid_sort_field