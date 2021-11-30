from enum import Enum


class ConnectionStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DEPRECATED = "deprecated"

    def __str__(self) -> str:
        return str(self.value)
