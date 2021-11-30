from enum import Enum


class CheckOperationReadStatus(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
