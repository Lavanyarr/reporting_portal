'''

TODO:
 i/p user_ids
 o/p user details:
        id
        name
        profile_pic
        user_role
        phone_no
'''

from typing import List

from reporting_portal_auth.exceptions.exceptions import InvalidUserIds
from reporting_portal_auth.interactors.storages.storage_interface \
    import StorageInterface
from reporting_portal_auth.interactors.presenters.user_dtos_presenter_interface \
    import UserDetailsPresenterInterface


class UserDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = StorageInterface

    def user_details_wrapper(self, user_ids: List[int],
                             presenter: UserDetailsPresenterInterface):

        try:
            response = self.user_details(user_ids=user_ids)

        except InvalidUserIds:
            response = presenter.raise_invalid_user_ids_exception()

        return response

    def user_details(self, user_ids: List[int]):

        user_dtos = self.storage.get_user_dtos(user_ids=user_ids)
        return user_dtos
