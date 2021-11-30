from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.upload_read_status import UploadReadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadRead")


@attr.s(auto_attribs=True)
class UploadRead:
    """ """

    status: UploadReadStatus
    resource_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        resource_id = self.resource_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = UploadReadStatus(d.pop("status"))

        resource_id = d.pop("resourceId", UNSET)

        upload_read = cls(
            status=status,
            resource_id=resource_id,
        )

        upload_read.additional_properties = d
        return upload_read

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
