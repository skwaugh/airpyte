from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DestinationRead")


@attr.s(auto_attribs=True)
class DestinationRead:
    """ """

    destination_definition_id: str
    destination_id: str
    workspace_id: str
    connection_configuration: None
    name: str
    destination_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination_definition_id = self.destination_definition_id
        destination_id = self.destination_id
        workspace_id = self.workspace_id
        connection_configuration = None

        name = self.name
        destination_name = self.destination_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationDefinitionId": destination_definition_id,
                "destinationId": destination_id,
                "workspaceId": workspace_id,
                "connectionConfiguration": connection_configuration,
                "name": name,
                "destinationName": destination_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_definition_id = d.pop("destinationDefinitionId")

        destination_id = d.pop("destinationId")

        workspace_id = d.pop("workspaceId")

        connection_configuration = None

        name = d.pop("name")

        destination_name = d.pop("destinationName")

        destination_read = cls(
            destination_definition_id=destination_definition_id,
            destination_id=destination_id,
            workspace_id=workspace_id,
            connection_configuration=connection_configuration,
            name=name,
            destination_name=destination_name,
        )

        destination_read.additional_properties = d
        return destination_read

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
