from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from reporting_portal.storages.storage_implementation \
    import StorageImplementation
from reporting_portal.presenters.category_presenter_implementation \
    import CategoryPresenterImplementation
from reporting_portal.interactors.categories_with_subcategories_interactor \
    import CategoriesWithSubCategoriesInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = StorageImplementation()
    presenter = CategoryPresenterImplementation()

    interactor = CategoriesWithSubCategoriesInteractor(
        storage=storage
    )
    response = interactor.get_categories_with_subcategories_wrapper(
        presenter=presenter
    )
    return response
