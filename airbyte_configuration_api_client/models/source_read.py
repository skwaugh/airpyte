from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceRead")


@attr.s(auto_attribs=True)
class SourceRead:
    """ """

    source_definition_id: str
    source_id: str
    workspace_id: str
    connection_configuration: None
    name: str
    source_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_definition_id = self.source_definition_id
        source_id = self.source_id
        workspace_id = self.workspace_id
        connection_configuration = None

        name = self.name
        source_name = self.source_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDefinitionId": source_definition_id,
                "sourceId": source_id,
                "workspaceId": workspace_id,
                "connectionConfiguration": connection_configuration,
                "name": name,
                "sourceName": source_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definition_id = d.pop("sourceDefinitionId")

        source_id = d.pop("sourceId")

        workspace_id = d.pop("workspaceId")

        connection_configuration = None

        name = d.pop("name")

        source_name = d.pop("sourceName")

        source_read = cls(
            source_definition_id=source_definition_id,
            source_id=source_id,
            workspace_id=workspace_id,
            connection_configuration=connection_configuration,
            name=name,
            source_name=source_name,
        )

        source_read.additional_properties = d
        return source_read

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
