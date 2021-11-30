from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.destination_definition_read import DestinationDefinitionRead

T = TypeVar("T", bound="DestinationDefinitionReadList")


@attr.s(auto_attribs=True)
class DestinationDefinitionReadList:
    """ """

    destination_definitions: List[DestinationDefinitionRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination_definitions = []
        for destination_definitions_item_data in self.destination_definitions:
            destination_definitions_item = destination_definitions_item_data.to_dict()

            destination_definitions.append(destination_definitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationDefinitions": destination_definitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_definitions = []
        _destination_definitions = d.pop("destinationDefinitions")
        for destination_definitions_item_data in _destination_definitions:
            destination_definitions_item = DestinationDefinitionRead.from_dict(destination_definitions_item_data)

            destination_definitions.append(destination_definitions_item)

        destination_definition_read_list = cls(
            destination_definitions=destination_definitions,
        )

        destination_definition_read_list.additional_properties = d
        return destination_definition_read_list

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
