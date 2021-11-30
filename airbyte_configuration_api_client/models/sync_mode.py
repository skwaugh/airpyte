from enum import Enum


class SyncMode(str, Enum):
    FULL_REFRESH = "full_refresh"
    INCREMENTAL = "incremental"

    def __str__(self) -> str:
        return str(self.value)
