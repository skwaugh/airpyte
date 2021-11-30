from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_schedule import ConnectionSchedule
from ..models.connection_status import ConnectionStatus
from ..models.destination_search import DestinationSearch
from ..models.namespace_definition_type import NamespaceDefinitionType
from ..models.source_search import SourceSearch
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebBackendConnectionSearch")


@attr.s(auto_attribs=True)
class WebBackendConnectionSearch:
    """ """

    connection_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespace_definition: Union[Unset, NamespaceDefinitionType] = NamespaceDefinitionType.SOURCE
    namespace_format: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    source_id: Union[Unset, str] = UNSET
    destination_id: Union[Unset, str] = UNSET
    schedule: Union[Unset, ConnectionSchedule] = UNSET
    status: Union[Unset, ConnectionStatus] = UNSET
    source: Union[Unset, SourceSearch] = UNSET
    destination: Union[Unset, DestinationSearch] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        name = self.name
        namespace_definition: Union[Unset, str] = UNSET
        if not isinstance(self.namespace_definition, Unset):
            namespace_definition = self.namespace_definition.value

        namespace_format = self.namespace_format
        prefix = self.prefix
        source_id = self.source_id
        destination_id = self.destination_id
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        destination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if name is not UNSET:
            field_dict["name"] = name
        if namespace_definition is not UNSET:
            field_dict["namespaceDefinition"] = namespace_definition
        if namespace_format is not UNSET:
            field_dict["namespaceFormat"] = namespace_format
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if destination_id is not UNSET:
            field_dict["destinationId"] = destination_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId", UNSET)

        name = d.pop("name", UNSET)

        _namespace_definition = d.pop("namespaceDefinition", UNSET)
        namespace_definition: Union[Unset, NamespaceDefinitionType]
        if isinstance(_namespace_definition, Unset):
            namespace_definition = UNSET
        else:
            namespace_definition = NamespaceDefinitionType(_namespace_definition)

        namespace_format = d.pop("namespaceFormat", UNSET)

        prefix = d.pop("prefix", UNSET)

        source_id = d.pop("sourceId", UNSET)

        destination_id = d.pop("destinationId", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ConnectionSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ConnectionSchedule.from_dict(_schedule)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ConnectionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ConnectionStatus(_status)

        _source = d.pop("source", UNSET)
        source: Union[Unset, SourceSearch]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SourceSearch.from_dict(_source)

        _destination = d.pop("destination", UNSET)
        destination: Union[Unset, DestinationSearch]
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = DestinationSearch.from_dict(_destination)

        web_backend_connection_search = cls(
            connection_id=connection_id,
            name=name,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            prefix=prefix,
            source_id=source_id,
            destination_id=destination_id,
            schedule=schedule,
            status=status,
            source=source,
            destination=destination,
        )

        web_backend_connection_search.additional_properties = d
        return web_backend_connection_search

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
