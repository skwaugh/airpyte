from enum import Enum


class AdvancedAuthAuthFlowType(str, Enum):
    OAUTH20 = "oauth2.0"
    OAUTH10 = "oauth1.0"

    def __str__(self) -> str:
        return str(self.value)
