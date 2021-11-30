from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.attempt_info_read import AttemptInfoRead
from ..models.job_read import JobRead

T = TypeVar("T", bound="JobInfoRead")


@attr.s(auto_attribs=True)
class JobInfoRead:
    """ """

    job: JobRead
    attempts: List[AttemptInfoRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job = self.job.to_dict()

        attempts = []
        for attempts_item_data in self.attempts:
            attempts_item = attempts_item_data.to_dict()

            attempts.append(attempts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job": job,
                "attempts": attempts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job = JobRead.from_dict(d.pop("job"))

        attempts = []
        _attempts = d.pop("attempts")
        for attempts_item_data in _attempts:
            attempts_item = AttemptInfoRead.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        job_info_read = cls(
            job=job,
            attempts=attempts,
        )

        job_info_read.additional_properties = d
        return job_info_read

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
