from ib_common.service_adapter_utils.base_adapter_class import BaseAdapterClass


class ServiceAdapter:

    @property
    def auth_service(self):
        from .auth_service import AuthService
        return AuthService()


def get_service_adapter():
    return ServiceAdapter()


