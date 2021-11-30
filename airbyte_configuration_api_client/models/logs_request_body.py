from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.log_type import LogType

T = TypeVar("T", bound="LogsRequestBody")


@attr.s(auto_attribs=True)
class LogsRequestBody:
    """ """

    log_type: LogType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        log_type = self.log_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logType": log_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_type = LogType(d.pop("logType"))

        logs_request_body = cls(
            log_type=log_type,
        )

        logs_request_body.additional_properties = d
        return logs_request_body

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
