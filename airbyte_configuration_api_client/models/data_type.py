from enum import Enum


class DataType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    OBJECT = "object"
    ARRAY = "array"

    def __str__(self) -> str:
        return str(self.value)
