import dataclasses
import datetime
from reporting_portal_auth.interactors.storages.storage_interface \
    import StorageInterface
from reporting_portal_auth.interactors.presenters.presenter_interface \
    import PresenterInterface
from reporting_portal_auth.exceptions.exceptions import (
    InvalidUserName,
    InvalidPassword
)
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage
from reporting_portal_auth.constants.enums import Role
from reporting_portal_auth.tests.storages.dtos import (
    UserAuthTokensDTO,
    UserDTO
)


class LoginInteractor:

    def __init__(self, storage: StorageInterface,
                 oauth_storage: OAuth2SQLStorage):
        self.storage = storage
        self.auth_storage = oauth_storage

    def user_login_wrapper(self, username: str,
                           password: str,
                           presenter: PresenterInterface):
        try:
            user_dto = self.user_login(username=username,
                                       password=password)

            return presenter.get_user_token_response(user_dto)

        except InvalidUserName:
            presenter.raise_invalid_user_name_exception(username=username)
        except InvalidPassword:
            presenter.raise_invalid_password_exception(password=password)

    def user_login(self, username: str, password: str):

        self.storage.validate_user_name(username=username)
        user_id = self.storage.validate_password(username=username,
                                                 password=password)
        role = self.storage.get_user_role(user_id=user_id)
        service = OAuthUserAuthTokensService(oauth2_storage=self.auth_storage)
        user_token_dto = service.create_user_auth_tokens(user_id)
        user_dto = UserDTO(
            user_token_dto=user_token_dto,
            user_role=role
        )

        return user_dto
