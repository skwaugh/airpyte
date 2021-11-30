from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification_read_status import NotificationReadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationRead")


@attr.s(auto_attribs=True)
class NotificationRead:
    """ """

    status: NotificationReadStatus
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
        status = NotificationReadStatus(d.pop("status"))

        message = d.pop("message", UNSET)

        notification_read = cls(
            status=status,
            message=message,
        )

        notification_read.additional_properties = d
        return notification_read

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
