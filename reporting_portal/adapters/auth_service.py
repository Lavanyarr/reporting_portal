from typing import List


class AuthService:

    @property
    def interface(self):
        from reporting_portal_auth.interfaces.service_interface \
            import ServiceInterface
        return ServiceInterface()

    # we use this function in this app

    def get_user_dtos(self, user_ids: List[int]):
        user_dtos = self.interface.get_user_dtos(user_ids=user_ids)
        return user_dtos
