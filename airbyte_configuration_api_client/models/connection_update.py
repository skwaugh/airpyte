from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.airbyte_catalog import AirbyteCatalog
from ..models.connection_schedule import ConnectionSchedule
from ..models.connection_status import ConnectionStatus
from ..models.namespace_definition_type import NamespaceDefinitionType
from ..models.resource_requirements import ResourceRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionUpdate")


@attr.s(auto_attribs=True)
class ConnectionUpdate:
    """ """

    connection_id: str
    sync_catalog: AirbyteCatalog
    status: ConnectionStatus
    namespace_definition: Union[Unset, NamespaceDefinitionType] = NamespaceDefinitionType.SOURCE
    namespace_format: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    operation_ids: Union[Unset, List[str]] = UNSET
    schedule: Union[Unset, ConnectionSchedule] = UNSET
    resource_requirements: Union[Unset, ResourceRequirements] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        sync_catalog = self.sync_catalog.to_dict()

        status = self.status.value

        namespace_definition: Union[Unset, str] = UNSET
        if not isinstance(self.namespace_definition, Unset):
            namespace_definition = self.namespace_definition.value

        namespace_format = self.namespace_format
        prefix = self.prefix
        operation_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operation_ids, Unset):
            operation_ids = self.operation_ids

        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        resource_requirements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource_requirements, Unset):
            resource_requirements = self.resource_requirements.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "syncCatalog": sync_catalog,
                "status": status,
            }
        )
        if namespace_definition is not UNSET:
            field_dict["namespaceDefinition"] = namespace_definition
        if namespace_format is not UNSET:
            field_dict["namespaceFormat"] = namespace_format
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if operation_ids is not UNSET:
            field_dict["operationIds"] = operation_ids
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if resource_requirements is not UNSET:
            field_dict["resourceRequirements"] = resource_requirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        sync_catalog = AirbyteCatalog.from_dict(d.pop("syncCatalog"))

        status = ConnectionStatus(d.pop("status"))

        _namespace_definition = d.pop("namespaceDefinition", UNSET)
        namespace_definition: Union[Unset, NamespaceDefinitionType]
        if isinstance(_namespace_definition, Unset):
            namespace_definition = UNSET
        else:
            namespace_definition = NamespaceDefinitionType(_namespace_definition)

        namespace_format = d.pop("namespaceFormat", UNSET)

        prefix = d.pop("prefix", UNSET)

        operation_ids = cast(List[str], d.pop("operationIds", UNSET))

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ConnectionSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ConnectionSchedule.from_dict(_schedule)

        _resource_requirements = d.pop("resourceRequirements", UNSET)
        resource_requirements: Union[Unset, ResourceRequirements]
        if isinstance(_resource_requirements, Unset):
            resource_requirements = UNSET
        else:
            resource_requirements = ResourceRequirements.from_dict(_resource_requirements)

        connection_update = cls(
            connection_id=connection_id,
            sync_catalog=sync_catalog,
            status=status,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            prefix=prefix,
            operation_ids=operation_ids,
            schedule=schedule,
            resource_requirements=resource_requirements,
        )

        connection_update.additional_properties = d
        return connection_update

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
