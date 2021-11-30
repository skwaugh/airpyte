from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attempt_status import AttemptStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttemptRead")


@attr.s(auto_attribs=True)
class AttemptRead:
    """ """

    id: int
    status: AttemptStatus
    created_at: int
    updated_at: int
    ended_at: Union[Unset, int] = UNSET
    bytes_synced: Union[Unset, int] = UNSET
    records_synced: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        created_at = self.created_at
        updated_at = self.updated_at
        ended_at = self.ended_at
        bytes_synced = self.bytes_synced
        records_synced = self.records_synced

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if bytes_synced is not UNSET:
            field_dict["bytesSynced"] = bytes_synced
        if records_synced is not UNSET:
            field_dict["recordsSynced"] = records_synced

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = AttemptStatus(d.pop("status"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        ended_at = d.pop("endedAt", UNSET)

        bytes_synced = d.pop("bytesSynced", UNSET)

        records_synced = d.pop("recordsSynced", UNSET)

        attempt_read = cls(
            id=id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            ended_at=ended_at,
            bytes_synced=bytes_synced,
            records_synced=records_synced,
        )

        attempt_read.additional_properties = d
        return attempt_read

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
