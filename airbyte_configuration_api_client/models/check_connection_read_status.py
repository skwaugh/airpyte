from enum import Enum


class CheckConnectionReadStatus(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
