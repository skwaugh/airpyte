from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.job_config_type import JobConfigType
from ..models.pagination import Pagination
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobListRequestBody")


@attr.s(auto_attribs=True)
class JobListRequestBody:
    """ """

    config_types: List[JobConfigType]
    config_id: str
    pagination: Union[Unset, Pagination] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_types = []
        for config_types_item_data in self.config_types:
            config_types_item = config_types_item_data.value

            config_types.append(config_types_item)

        config_id = self.config_id
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configTypes": config_types,
                "configId": config_id,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_types = []
        _config_types = d.pop("configTypes")
        for config_types_item_data in _config_types:
            config_types_item = JobConfigType(config_types_item_data)

            config_types.append(config_types_item)

        config_id = d.pop("configId")

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        job_list_request_body = cls(
            config_types=config_types,
            config_id=config_id,
            pagination=pagination,
        )

        job_list_request_body.additional_properties = d
        return job_list_request_body

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
