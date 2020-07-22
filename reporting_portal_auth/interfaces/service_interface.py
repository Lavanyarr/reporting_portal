from typing import List

from reporting_portal_auth.interactors.UserDetailsInteractor \
    import UserDetailsInteractor
from reporting_portal_auth.storages.storage_implementation \
    import StorageImplementation


class ServiceInterface:

    @staticmethod
    def get_user_dtos(user_ids: List[int]):
        storage = StorageImplementation()
        interactor = UserDetailsInteractor(storage=storage)
        user_dtos = interactor.user_details(user_ids=user_ids)

        return user_dtos
