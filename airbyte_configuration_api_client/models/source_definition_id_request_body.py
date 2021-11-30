from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceDefinitionIdRequestBody")


@attr.s(auto_attribs=True)
class SourceDefinitionIdRequestBody:
    """ """

    source_definition_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_definition_id = self.source_definition_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDefinitionId": source_definition_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definition_id = d.pop("sourceDefinitionId")

        source_definition_id_request_body = cls(
            source_definition_id=source_definition_id,
        )

        source_definition_id_request_body.additional_properties = d
        return source_definition_id_request_body

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
