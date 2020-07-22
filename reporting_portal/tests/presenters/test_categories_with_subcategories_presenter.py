'''

TODO: categories are not there
TODO: categories are therer but sub categories are not therer
TODO: both are present
'''

import json

import pytest
from reporting_portal.presenters.category_presenter_implementation import \
    CategoryPresenterImplementation
from reporting_portal.interactors.storages.dtos import \
    CategoryWithSubCategoryDTO
from reporting_portal.tests.factories.storage_factories import (
    CategoryFactory,
    SubCategoryFactory
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

        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(1)

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

        CategoryFactory.reset_sequence()
        category = CategoryFactory.create_batch(1)
        SubCategoryFactory.reset_sequence()
        subcategory = SubCategoryFactory.create_batch(2, category_id=category[0])

        response_dto = CategoryWithSubCategoryDTO(
            category_dto=category,
            subcategory_dto=subcategory
        )

        # act
        response = presenter.get_categories_with_subacategories_response(response_dto)

        # assert
        data = json.loads(response.content)
        snapshot.assert_match(data, 'categories_with_sub_categories_dto')
