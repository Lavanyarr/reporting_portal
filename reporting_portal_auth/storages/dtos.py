import dataclasses

from reporting_portal_auth.constants.enums import Role


@dataclasses.dataclass()
class UserDTO:
    id: int
    name: str
    phone_no: int
    profile_pic: str
    user_role: Role
