from enum import Enum


class OperatorNormalizationOption(str, Enum):
    BASIC = "basic"

    def __str__(self) -> str:
        return str(self.value)
