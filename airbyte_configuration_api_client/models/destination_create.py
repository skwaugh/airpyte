from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DestinationCreate")


@attr.s(auto_attribs=True)
class DestinationCreate:
    """ """

    workspace_id: str
    name: str
    destination_definition_id: str
    connection_configuration: None
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace_id = self.workspace_id
        name = self.name
        destination_definition_id = self.destination_definition_id
        connection_configuration = None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "destinationDefinitionId": destination_definition_id,
                "connectionConfiguration": connection_configuration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        destination_definition_id = d.pop("destinationDefinitionId")

        connection_configuration = None

        destination_create = cls(
            workspace_id=workspace_id,
            name=name,
            destination_definition_id=destination_definition_id,
            connection_configuration=connection_configuration,
        )

        destination_create.additional_properties = d
        return destination_create

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
