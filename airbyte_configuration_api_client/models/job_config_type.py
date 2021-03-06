from enum import Enum


class JobConfigType(str, Enum):
    CHECK_CONNECTION_SOURCE = "check_connection_source"
    CHECK_CONNECTION_DESTINATION = "check_connection_destination"
    DISCOVER_SCHEMA = "discover_schema"
    GET_SPEC = "get_spec"
    SYNC = "sync"
    RESET_CONNECTION = "reset_connection"

    def __str__(self) -> str:
        return str(self.value)
