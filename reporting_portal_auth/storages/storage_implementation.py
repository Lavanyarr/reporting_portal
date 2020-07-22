from reporting_portal_auth.interactors.storages.storage_interface import \
    StorageInterface
from reporting_portal_auth.exceptions.exceptions import (
    InvalidUserName,
    InvalidPassword
)
from reporting_portal_auth.models import User
from reporting_portal_auth.storages.dtos import UserDTO
from typing import List


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

    def get_user_dtos(self, user_ids: List[int]):

        user_objs = User.objects.filter(id__in=user_ids)
        user_dtos_list = []

        for user in user_objs:
            user_dto = self.convert_user_obj_to_dto(user)
            user_dtos_list.append(user_dto)

        return user_dtos_list

    @staticmethod
    def convert_user_obj_to_dto(user):
        user_dto = UserDTO(
            id=user.id,
            name=user.name,
            profile_pic=user.profile_pic,
            role=user.role,
            phone_no=user.phone_no
        )
        return user_dto


