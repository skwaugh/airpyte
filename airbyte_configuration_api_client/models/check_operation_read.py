from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.check_operation_read_status import CheckOperationReadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckOperationRead")


@attr.s(auto_attribs=True)
class CheckOperationRead:
    """ """

    status: CheckOperationReadStatus
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = CheckOperationReadStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        check_operation_read = cls(
            status=status,
            message=message,
        )

        check_operation_read.additional_properties = d
        return check_operation_read

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
