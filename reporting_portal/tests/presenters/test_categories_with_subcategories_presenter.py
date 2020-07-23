import json

import pytest
from reporting_portal.presenters.category_presenter_implementation import \
    CategoryPresenterImplementation
from reporting_portal.interactors.storages.dtos import \
    CategoryWithSubCategoryDTO
from reporting_portal.tests.factories.dto_factories import (
    CategoryDTOFactory,
    SubCategoryDTOFactory
)



@pytest.mark.django_db
class TestCategoriesWithSubCategoriesPresenter:

    def test_categories_when_there_are_no_categories(self, snapshot):
        # arrange
        presenter = CategoryPresenterImplementation()

        response_dto = CategoryWithSubCategoryDTO(
            category_dto=[],
            subcategory_dto=[]
        )

        # act
        response = presenter.get_categories_with_subacategories_response(response_dto)


        # assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'empty_dict')

    def test_categories_when_there_are_categories_but_no_subcategories(self, snapshot):
        # arrange
        presenter = CategoryPresenterImplementation()

        CategoryDTOFactory.reset_sequence()
        category = CategoryDTOFactory.create_batch(1)

        response_dto = CategoryWithSubCategoryDTO(
            category_dto=category,
            subcategory_dto=[]
        )

        # act
        response = presenter.get_categories_with_subacategories_response(response_dto)

        # assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'categories_with_empty_sub_categories_dto')

    def test_categories_when_there_are_categories(self, snapshot):
        # arrange
        presenter = CategoryPresenterImplementation()

        CategoryDTOFactory.reset_sequence()
        category = CategoryDTOFactory.create_batch(1)
        SubCategoryDTOFactory.reset_sequence()
        subcategory = SubCategoryDTOFactory.create_batch(2, category_id=1)

        response_dto = CategoryWithSubCategoryDTO(
            category_dto=category,
            subcategory_dto=subcategory
        )

        # act
        response = presenter.get_categories_with_subacategories_response(response_dto)

        # assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'categories_with_sub_categories_dto')