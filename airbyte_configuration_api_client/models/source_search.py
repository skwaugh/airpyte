from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceSearch")


@attr.s(auto_attribs=True)
class SourceSearch:
    """ """

    source_definition_id: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    connection_configuration: Union[Unset, None] = UNSET
    name: Union[Unset, str] = UNSET
    source_name: Union[Unset, str] = UNSET
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
        field_dict.update({})
        if source_definition_id is not UNSET:
            field_dict["sourceDefinitionId"] = source_definition_id
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if connection_configuration is not UNSET:
            field_dict["connectionConfiguration"] = connection_configuration
        if name is not UNSET:
            field_dict["name"] = name
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definition_id = d.pop("sourceDefinitionId", UNSET)

        source_id = d.pop("sourceId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        connection_configuration = None

        name = d.pop("name", UNSET)

        source_name = d.pop("sourceName", UNSET)

        source_search = cls(
            source_definition_id=source_definition_id,
            source_id=source_id,
            workspace_id=workspace_id,
            connection_configuration=connection_configuration,
            name=name,
            source_name=source_name,
        )

        source_search.additional_properties = d
        return source_search

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
