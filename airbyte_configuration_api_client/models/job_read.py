from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.job_config_type import JobConfigType
from ..models.job_status import JobStatus

T = TypeVar("T", bound="JobRead")


@attr.s(auto_attribs=True)
class JobRead:
    """ """

    id: int
    config_type: JobConfigType
    config_id: str
    created_at: int
    updated_at: int
    status: JobStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        config_type = self.config_type.value

        config_id = self.config_id
        created_at = self.created_at
        updated_at = self.updated_at
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "configType": config_type,
                "configId": config_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        config_type = JobConfigType(d.pop("configType"))

        config_id = d.pop("configId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        status = JobStatus(d.pop("status"))

        job_read = cls(
            id=id,
            config_type=config_type,
            config_id=config_id,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
        )

        job_read.additional_properties = d
        return job_read

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
