from enum import Enum


class ConnectionScheduleTimeUnit(str, Enum):
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"
    MONTHS = "months"

    def __str__(self) -> str:
        return str(self.value)
