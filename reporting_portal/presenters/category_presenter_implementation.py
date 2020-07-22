from django.http import response

from reporting_portal.interactors.presenters.categories_presenter_interface \
    import CategoriesPresenterInterface

from reporting_portal.interactors.storages.dtos import CategoryWithSubCategoryDTO


class CategoryPresenterImplementation(CategoriesPresenterInterface):

    def get_categories_with_subacategories_response(self, response_dto: CategoryWithSubCategoryDTO):
        import json
        response_object = response.HttpResponse(
            json.dumps({
                "categories": self.get_categories(response_dto)
            })
        )
        return response_object


    def get_categories(self, response_dto):
        categories_list = []
        category_dto = response_dto.category_dto
        subcategory_dto = response_dto.subcategory_dto

        for category in category_dto:
            category_dict = {
                "id": category.id,
                "name": category.name,
                "subcategories": self.get_subcategories(category.id, subcategory_dto)
            }
            categories_list.append(category_dict)
        return categories_list

    def get_subcategories(self, category_id, subcategory_dto):
        sub_categories_list = []

        for sub_category in subcategory_dto:
            if category_id == sub_category.category_id.id:
                sub_category_dict = self.get_sub_category_details(sub_category)
                sub_categories_list.append(sub_category_dict)
        return sub_categories_list

    @staticmethod
    def get_sub_category_details(subcategory):
        sub_category_dict = {
            "id": subcategory.id,

            "name": subcategory.name
        }
        return sub_category_dict
