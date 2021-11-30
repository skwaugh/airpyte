from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.source_definition_read import SourceDefinitionRead

T = TypeVar("T", bound="SourceDefinitionReadList")


@attr.s(auto_attribs=True)
class SourceDefinitionReadList:
    """ """

    source_definitions: List[SourceDefinitionRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_definitions = []
        for source_definitions_item_data in self.source_definitions:
            source_definitions_item = source_definitions_item_data.to_dict()

            source_definitions.append(source_definitions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDefinitions": source_definitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definitions = []
        _source_definitions = d.pop("sourceDefinitions")
        for source_definitions_item_data in _source_definitions:
            source_definitions_item = SourceDefinitionRead.from_dict(source_definitions_item_data)

            source_definitions.append(source_definitions_item)

        source_definition_read_list = cls(
            source_definitions=source_definitions,
        )

        source_definition_read_list.additional_properties = d
        return source_definition_read_list

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
