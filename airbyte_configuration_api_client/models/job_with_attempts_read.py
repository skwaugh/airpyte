from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attempt_read import AttemptRead
from ..models.job_read import JobRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobWithAttemptsRead")


@attr.s(auto_attribs=True)
class JobWithAttemptsRead:
    """ """

    job: Union[Unset, JobRead] = UNSET
    attempts: Union[Unset, List[AttemptRead]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job, Unset):
            job = self.job.to_dict()

        attempts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attempts, Unset):
            attempts = []
            for attempts_item_data in self.attempts:
                attempts_item = attempts_item_data.to_dict()

                attempts.append(attempts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job is not UNSET:
            field_dict["job"] = job
        if attempts is not UNSET:
            field_dict["attempts"] = attempts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _job = d.pop("job", UNSET)
        job: Union[Unset, JobRead]
        if isinstance(_job, Unset):
            job = UNSET
        else:
            job = JobRead.from_dict(_job)

        attempts = []
        _attempts = d.pop("attempts", UNSET)
        for attempts_item_data in _attempts or []:
            attempts_item = AttemptRead.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        job_with_attempts_read = cls(
            job=job,
            attempts=attempts,
        )

        job_with_attempts_read.additional_properties = d
        return job_with_attempts_read

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
