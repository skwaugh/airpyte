from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceRequirements")


@attr.s(auto_attribs=True)
class ResourceRequirements:
    """optional resource requirements to run workers (blank for unbounded allocations)"""

    cpu_request: Union[Unset, str] = UNSET
    cpu_limit: Union[Unset, str] = UNSET
    memory_request: Union[Unset, str] = UNSET
    memory_limit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu_request = self.cpu_request
        cpu_limit = self.cpu_limit
        memory_request = self.memory_request
        memory_limit = self.memory_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_request is not UNSET:
            field_dict["cpu_request"] = cpu_request
        if cpu_limit is not UNSET:
            field_dict["cpu_limit"] = cpu_limit
        if memory_request is not UNSET:
            field_dict["memory_request"] = memory_request
        if memory_limit is not UNSET:
            field_dict["memory_limit"] = memory_limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu_request = d.pop("cpu_request", UNSET)

        cpu_limit = d.pop("cpu_limit", UNSET)

        memory_request = d.pop("memory_request", UNSET)

        memory_limit = d.pop("memory_limit", UNSET)

        resource_requirements = cls(
            cpu_request=cpu_request,
            cpu_limit=cpu_limit,
            memory_request=memory_request,
            memory_limit=memory_limit,
        )

        resource_requirements.additional_properties = d
        return resource_requirements

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
