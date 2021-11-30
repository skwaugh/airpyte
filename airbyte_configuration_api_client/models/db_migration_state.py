from enum import Enum


class DbMigrationState(str, Enum):
    PENDING = "pending"
    ABOVE_TARGET = "above_target"
    BELOW_BASELINE = "below_baseline"
    BASELINE = "baseline"
    IGNORED = "ignored"
    MISSING_SUCCESS = "missing_success"
    MISSING_FAILED = "missing_failed"
    SUCCESS = "success"
    UNDONE = "undone"
    AVAILABLE = "available"
    FAILED = "failed"
    OUT_OF_ORDER = "out_of_order"
    FUTURE_SUCCESS = "future_success"
    FUTURE_FAILED = "future_failed"
    OUTDATED = "outdated"
    SUPERSEDED = "superseded"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
