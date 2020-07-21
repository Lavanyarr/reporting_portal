from ib_common.constants import BaseEnumClass
import enum

class Role(BaseEnumClass, enum.Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'
    RP = 'RP'
