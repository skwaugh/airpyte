from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceCreate")


@attr.s(auto_attribs=True)
class SourceCreate:
    """ """

    source_definition_id: str
    connection_configuration: None
    workspace_id: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_definition_id = self.source_definition_id
        connection_configuration = None

        workspace_id = self.workspace_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDefinitionId": source_definition_id,
                "connectionConfiguration": connection_configuration,
                "workspaceId": workspace_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definition_id = d.pop("sourceDefinitionId")

        connection_configuration = None

        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        source_create = cls(
            source_definition_id=source_definition_id,
            connection_configuration=connection_configuration,
            workspace_id=workspace_id,
            name=name,
        )

        source_create.additional_properties = d
        return source_create

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
