from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.job_with_attempts_read import JobWithAttemptsRead

T = TypeVar("T", bound="JobReadList")


@attr.s(auto_attribs=True)
class JobReadList:
    """ """

    jobs: List[JobWithAttemptsRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item = jobs_item_data.to_dict()

            jobs.append(jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:
            jobs_item = JobWithAttemptsRead.from_dict(jobs_item_data)

            jobs.append(jobs_item)

        job_read_list = cls(
            jobs=jobs,
        )

        job_read_list.additional_properties = d
        return job_read_list

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
