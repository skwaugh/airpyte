from enum import Enum


class ImportReadStatus(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
