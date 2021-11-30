from enum import Enum


class NotificationType(str, Enum):
    SLACK = "slack"

    def __str__(self) -> str:
        return str(self.value)
