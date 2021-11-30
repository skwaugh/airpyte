from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.check_connection_read_status import CheckConnectionReadStatus
from ..models.synchronous_job_read import SynchronousJobRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckConnectionRead")


@attr.s(auto_attribs=True)
class CheckConnectionRead:
    """ """

    status: CheckConnectionReadStatus
    job_info: SynchronousJobRead
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        job_info = self.job_info.to_dict()

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "jobInfo": job_info,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = CheckConnectionReadStatus(d.pop("status"))

        job_info = SynchronousJobRead.from_dict(d.pop("jobInfo"))

        message = d.pop("message", UNSET)

        check_connection_read = cls(
            status=status,
            job_info=job_info,
            message=message,
        )

        check_connection_read.additional_properties = d
        return check_connection_read

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
