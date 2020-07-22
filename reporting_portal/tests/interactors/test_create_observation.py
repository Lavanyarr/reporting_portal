'''

TODO:

 i/p: {
  "title": "string",
  "category_id": 0,
  "sub_category_id": 0,
  "severity": [
    "HIGH"
  ],
  "description": "string",
  "attachments": [
    "string"
  ]
}
o/p :
success response

failure cases:
     invalid category_id
     invalid subcategory id for category
'''

import pytest
from unittest.mock import create_autospec

from reporting_portal.interactors.create_observation_interactor import CreateObservationInteractor
from reporting_portal.exceptions.exceptions import InvalidCategoryId, InvalidSubCategoryId


class TestCreateObservationInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from reporting_portal.interactors.storages.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from reporting_portal.interactors.presenters.observation_presenter_interface \
            import ObservationPresenterInterface

        presenter = create_autospec(ObservationPresenterInterface)
        return presenter

    def test_create_observation_when_given_category_id_is_invalid(self,
                                                                  storage_mock,
                                                                  presenter_mock):
        # arrange
        from reporting_portal.interactors.storages.dtos import ObservationDTO
        interactor = CreateObservationInteractor(
            storage=storage_mock
        )
        storage_mock.validate_category_id.return_value = InvalidCategoryId
        observation_dto = ObservationDTO(
            title='hello',
            category_id=10,
            subcategory_id=1,
            severity='HIGH',
            description='hello',
            attachments=["hello"]
        )
        # act
        response = interactor.create_observation_wrapper(
            observation_dto,
            presenter=presenter_mock
        )

        # assert
        storage_mock.validate_category_id.assert_called_once_with(observation_dto.category_id)

    def test_create_observation_when_given_sub_category_id_is_invalid(self,
                                                                      storage_mock,
                                                                      presenter_mock):
        # arrange
        from reporting_portal.interactors.storages.dtos import ObservationDTO
        interactor = CreateObservationInteractor(
            storage=storage_mock
        )
        storage_mock.validate_subcategory_id.return_value = InvalidSubCategoryId
        observation_dto = ObservationDTO(
            title='hello',
            category_id=1,
            subcategory_id=10,
            severity='HIGH',
            description='hello',
            attachments=["hello"]
        )
        # act
        response = interactor.create_observation_wrapper(
            observation_dto,
            presenter=presenter_mock
        )

        # assert
        storage_mock.validate_subcategory_id.assert_called_once_with(observation_dto.category_id,
                                                                     observation_dto.subcategory_id)

    def test_create_observation_when_given_details_are_valid(self,
                                                             storage_mock,
                                                             presenter_mock):
        # arrange
        from reporting_portal.interactors.storages.dtos import ObservationDTO
        interactor = CreateObservationInteractor(
            storage=storage_mock
        )
        observation_dto = ObservationDTO(
            title='hello',
            category_id=1,
            subcategory_id=10,
            severity='HIGH',
            description='hello',
            attachments=["hello"]
        )
        # act
        response = interactor.create_observation_wrapper(
            observation_dto,
            presenter=presenter_mock
        )

        # assert
        storage_mock.validate_category_id.assert_called_once_with(observation_dto.category_id)
        storage_mock.validate_subcategory_id.assert_called_once_with(observation_dto.category_id,
                                                                     observation_dto.subcategory_id)
        storage_mock.create_observation.assert_called_once_with(observation_dto)
