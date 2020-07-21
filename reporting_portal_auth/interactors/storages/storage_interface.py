import abc
from reporting_portal_auth.constants.enums import Role

class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_user_name(self, username: str):
        pass

    @abc.abstractmethod
    def validate_password(self, username: str, password:str):
        pass

    @abc.abstractmethod
    def get_user_role(self, user_id: int)-> Role:
        pass