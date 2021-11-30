from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.destination_read import DestinationRead

T = TypeVar("T", bound="DestinationReadList")


@attr.s(auto_attribs=True)
class DestinationReadList:
    """ """

    destinations: List[DestinationRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destinations = []
        for destinations_item_data in self.destinations:
            destinations_item = destinations_item_data.to_dict()

            destinations.append(destinations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinations": destinations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destinations = []
        _destinations = d.pop("destinations")
        for destinations_item_data in _destinations:
            destinations_item = DestinationRead.from_dict(destinations_item_data)

            destinations.append(destinations_item)

        destination_read_list = cls(
            destinations=destinations,
        )

        destination_read_list.additional_properties = d
        return destination_read_list

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
