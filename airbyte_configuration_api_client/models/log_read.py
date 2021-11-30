from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="LogRead")


@attr.s(auto_attribs=True)
class LogRead:
    """ """

    log_lines: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        log_lines = self.log_lines

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logLines": log_lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_lines = cast(List[str], d.pop("logLines"))

        log_read = cls(
            log_lines=log_lines,
        )

        log_read.additional_properties = d
        return log_read

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
