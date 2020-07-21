import dataclasses
import datetime

from reporting_portal_auth.constants.enums import Role


@dataclasses.dataclass()
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires_in: datetime.datetime


@dataclasses.dataclass()
class UserDTO:
    user_token_dto: UserAuthTokensDTO
    user_role: Role
