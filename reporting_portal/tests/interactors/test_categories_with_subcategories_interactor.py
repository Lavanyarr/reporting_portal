'''

Get categories with sub categories
TODO:

    i/p: no input
    o/p: {
  "categories": [
    {
      "id": 0,
      "name": "string",
      "subcategories": [
        {
          "id": 0,
          "name": "string"
        }
      ]
    }
  ]
}

cases:
     when there is no catgorie sin database
     when there is no sub categoriy for a particular category


get list of categories
get list of subcategories (in subcategories list place category id ) and modify it accoeding in presenter implementation
'''

import pytest
from unittest.mock import create_autospec
from reporting_portal.interactors.categories_with_subcategories_interactor \
    import CategoriesWithSubCategoriesInteractor


class TestcategoriesWithSubCategoriesInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from reporting_portal.interactors.storages.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from reporting_portal.interactors.presenters.categories_presenter_interface \
            import CategoriesPresenterInterface

        presenter = create_autospec(CategoriesPresenterInterface)
        return presenter

    def test_get_categories_when_there_is_no_catgories_in_database(
            self, storage_mock, presenter_mock):
        # arrange
        interactor = CategoriesWithSubCategoriesInteractor(
            storage=storage_mock
        )
        storage_mock.get_categories_of_observation.return_value = []
        # act
        response = interactor.get_categories_with_subcategories_wrapper(
            presenter=presenter_mock
        )

        # assert
        storage_mock.get_categories_of_observation.assert_called_once()

    def test_get_categories_when_there_is_catgories_in_database(
            self, storage_mock, presenter_mock):
        # arrange
        interactor = CategoriesWithSubCategoriesInteractor(
            storage=storage_mock
        )
        from reporting_portal.tests.factories.dto_factories import CategoryDTOFactory
        CategoryDTOFactory.reset_sequence()
        category_dto = CategoryDTOFactory.create_batch(2)
        storage_mock.get_categories_of_observation.return_value = category_dto

        # act
        response = interactor.get_categories_with_subcategories_wrapper(
            presenter=presenter_mock
        )

        # assert
        storage_mock.get_categories_of_observation.assert_called_once()

    def test_get_sub_categories_when_there_is_catgories_in_database(
            self, storage_mock, presenter_mock):
        # arrange

        category_ids = [1, 2]
        interactor = CategoriesWithSubCategoriesInteractor(
            storage=storage_mock
        )
        from reporting_portal.tests.factories.dto_factories import CategoryDTOFactory

        CategoryDTOFactory.reset_sequence()
        category_dto = CategoryDTOFactory.create_batch(2)
        storage_mock.get_categories_of_observation.return_value = category_dto

        # act
        response = interactor.get_categories_with_subcategories_wrapper(
            presenter=presenter_mock
        )

        # assert
        storage_mock.get_categories_of_observation.assert_called_once()
        storage_mock.get_subcategories.assert_called_once_with(category_ids)
