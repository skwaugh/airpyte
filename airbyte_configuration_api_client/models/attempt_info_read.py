from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.attempt_read import AttemptRead
from ..models.log_read import LogRead

T = TypeVar("T", bound="AttemptInfoRead")


@attr.s(auto_attribs=True)
class AttemptInfoRead:
    """ """

    attempt: AttemptRead
    logs: LogRead
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attempt = self.attempt.to_dict()

        logs = self.logs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attempt": attempt,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attempt = AttemptRead.from_dict(d.pop("attempt"))

        logs = LogRead.from_dict(d.pop("logs"))

        attempt_info_read = cls(
            attempt=attempt,
            logs=logs,
        )

        attempt_info_read.additional_properties = d
        return attempt_info_read

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
