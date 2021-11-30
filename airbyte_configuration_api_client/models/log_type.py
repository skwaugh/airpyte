from enum import Enum


class LogType(str, Enum):
    SERVER = "server"
    SCHEDULER = "scheduler"

    def __str__(self) -> str:
        return str(self.value)
