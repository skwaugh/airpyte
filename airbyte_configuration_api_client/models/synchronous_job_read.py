from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.job_config_type import JobConfigType
from ..models.log_read import LogRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="SynchronousJobRead")


@attr.s(auto_attribs=True)
class SynchronousJobRead:
    """ """

    id: str
    config_type: JobConfigType
    created_at: int
    ended_at: int
    succeeded: bool
    config_id: Union[Unset, str] = UNSET
    logs: Union[Unset, LogRead] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        config_type = self.config_type.value

        created_at = self.created_at
        ended_at = self.ended_at
        succeeded = self.succeeded
        config_id = self.config_id
        logs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = self.logs.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "configType": config_type,
                "createdAt": created_at,
                "endedAt": ended_at,
                "succeeded": succeeded,
            }
        )
        if config_id is not UNSET:
            field_dict["configId"] = config_id
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        config_type = JobConfigType(d.pop("configType"))

        created_at = d.pop("createdAt")

        ended_at = d.pop("endedAt")

        succeeded = d.pop("succeeded")

        config_id = d.pop("configId", UNSET)

        _logs = d.pop("logs", UNSET)
        logs: Union[Unset, LogRead]
        if isinstance(_logs, Unset):
            logs = UNSET
        else:
            logs = LogRead.from_dict(_logs)

        synchronous_job_read = cls(
            id=id,
            config_type=config_type,
            created_at=created_at,
            ended_at=ended_at,
            succeeded=succeeded,
            config_id=config_id,
            logs=logs,
        )

        synchronous_job_read.additional_properties = d
        return synchronous_job_read

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
