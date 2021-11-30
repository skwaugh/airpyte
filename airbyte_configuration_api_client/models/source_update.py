from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceUpdate")


@attr.s(auto_attribs=True)
class SourceUpdate:
    """ """

    source_id: str
    connection_configuration: None
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_id = self.source_id
        connection_configuration = None

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceId": source_id,
                "connectionConfiguration": connection_configuration,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_id = d.pop("sourceId")

        connection_configuration = None

        name = d.pop("name")

        source_update = cls(
            source_id=source_id,
            connection_configuration=connection_configuration,
            name=name,
        )

        source_update.additional_properties = d
        return source_update

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
