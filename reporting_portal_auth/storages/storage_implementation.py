from reporting_portal_auth.interactors.storages.storage_interface import \
    StorageInterface
from reporting_portal_auth.exceptions.exceptions import (
    InvalidUserName,
    InvalidPassword
)
from reporting_portal_auth.models import User


class StorageImplementation(StorageInterface):

    def validate_user_name(self, username: str):

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName

    def validate_password(self, username: str, password: str):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName

        if not user.check_password(password):
            raise InvalidPassword

        return user.id

    def get_user_role(self, user_id: int):
        user = User.objects.get(id=user_id)
        return user.user_role
