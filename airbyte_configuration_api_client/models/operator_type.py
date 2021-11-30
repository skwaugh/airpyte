from enum import Enum


class OperatorType(str, Enum):
    NORMALIZATION = "normalization"
    DBT = "dbt"

    def __str__(self) -> str:
        return str(self.value)
