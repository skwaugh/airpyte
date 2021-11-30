from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DestinationSearch")


@attr.s(auto_attribs=True)
class DestinationSearch:
    """ """

    destination_definition_id: Union[Unset, str] = UNSET
    destination_id: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    connection_configuration: Union[Unset, None] = UNSET
    name: Union[Unset, str] = UNSET
    destination_name: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if destination_definition_id is not UNSET:
            field_dict["destinationDefinitionId"] = destination_definition_id
        if destination_id is not UNSET:
            field_dict["destinationId"] = destination_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if connection_configuration is not UNSET:
            field_dict["connectionConfiguration"] = connection_configuration
        if name is not UNSET:
            field_dict["name"] = name
        if destination_name is not UNSET:
            field_dict["destinationName"] = destination_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_definition_id = d.pop("destinationDefinitionId", UNSET)

        destination_id = d.pop("destinationId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        connection_configuration = None

        name = d.pop("name", UNSET)

        destination_name = d.pop("destinationName", UNSET)

        destination_search = cls(
            destination_definition_id=destination_definition_id,
            destination_id=destination_id,
            workspace_id=workspace_id,
            connection_configuration=connection_configuration,
            name=name,
            destination_name=destination_name,
        )

        destination_search.additional_properties = d
        return destination_search

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
