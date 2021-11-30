from enum import Enum


class AuthSpecificationAuthType(str, Enum):
    OAUTH20 = "oauth2.0"

    def __str__(self) -> str:
        return str(self.value)
