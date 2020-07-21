from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from reporting_portal_auth.storages.storage_implementation \
    import StorageImplementation
from reporting_portal_auth.presenters.presenter_implementation \
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from reporting_portal_auth.interactors.login_interactor import LoginInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauthstorage = OAuth2SQLStorage()

    interactors = LoginInteractor(
        storage=storage,
        oauth_storage=oauthstorage
    )

    result = interactors.user_login_wrapper(
        username=username,
        password=password,
        presenter=presenter
    )
    return result