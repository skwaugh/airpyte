from enum import Enum


class DestinationSyncMode(str, Enum):
    APPEND = "append"
    OVERWRITE = "overwrite"
    APPEND_DEDUP = "append_dedup"

    def __str__(self) -> str:
        return str(self.value)
