from enum import Enum


class NamespaceDefinitionType(str, Enum):
    SOURCE = "source"
    DESTINATION = "destination"
    CUSTOMFORMAT = "customformat"

    def __str__(self) -> str:
        return str(self.value)
