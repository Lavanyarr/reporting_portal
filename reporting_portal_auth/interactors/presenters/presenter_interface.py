import abc
from common.dtos import UserAuthTokensDTO
from django.http import response
import dataclasses

from reporting_portal_auth.constants.enums import Role


@dataclasses.dataclass()
class UserDTO:
    user_token_dto: UserAuthTokensDTO
    user_role: Role


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_user_name_exception(self, username):
        pass

    @abc.abstractmethod
    def raise_invalid_password_exception(self, password):
        pass

    @abc.abstractmethod
    def get_user_token_response(
            self, user_dto: UserDTO) -> response.HttpResponse:
        pass
