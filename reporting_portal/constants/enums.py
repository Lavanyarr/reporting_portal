import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"


class Status(BaseEnumClass, enum.Enum):
    ALL = "ALL"
    ACTION_IN_PROGRESS = "ACTION_IN_PROGRESS"
    ACKNOWLEDGE_BY = "ACKNOWLEDGE_BY"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"
    REPORTED = 'REPORTED'


class Severity(BaseEnumClass, enum.Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    WARNING = "WARNING"


class Sort(BaseEnumClass, enum.Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortField(BaseEnumClass, enum.Enum):
    REPORTED_ON = "REPORTED_ON"
    DUE_DATE = "DUE_DATE"
