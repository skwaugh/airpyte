from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.airbyte_catalog import AirbyteCatalog
from ..models.connection_schedule import ConnectionSchedule
from ..models.connection_status import ConnectionStatus
from ..models.destination_read import DestinationRead
from ..models.job_status import JobStatus
from ..models.namespace_definition_type import NamespaceDefinitionType
from ..models.operation_read import OperationRead
from ..models.resource_requirements import ResourceRequirements
from ..models.source_read import SourceRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebBackendConnectionRead")


@attr.s(auto_attribs=True)
class WebBackendConnectionRead:
    """ """

    connection_id: str
    name: str
    source_id: str
    destination_id: str
    sync_catalog: AirbyteCatalog
    status: ConnectionStatus
    source: SourceRead
    destination: DestinationRead
    is_syncing: bool
    namespace_definition: Union[Unset, NamespaceDefinitionType] = NamespaceDefinitionType.SOURCE
    namespace_format: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    schedule: Union[Unset, ConnectionSchedule] = UNSET
    operation_ids: Union[Unset, List[str]] = UNSET
    operations: Union[Unset, List[OperationRead]] = UNSET
    latest_sync_job_created_at: Union[Unset, int] = UNSET
    latest_sync_job_status: Union[Unset, JobStatus] = UNSET
    resource_requirements: Union[Unset, ResourceRequirements] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        name = self.name
        source_id = self.source_id
        destination_id = self.destination_id
        sync_catalog = self.sync_catalog.to_dict()

        status = self.status.value

        source = self.source.to_dict()

        destination = self.destination.to_dict()

        is_syncing = self.is_syncing
        namespace_definition: Union[Unset, str] = UNSET
        if not isinstance(self.namespace_definition, Unset):
            namespace_definition = self.namespace_definition.value

        namespace_format = self.namespace_format
        prefix = self.prefix
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        operation_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operation_ids, Unset):
            operation_ids = self.operation_ids

        operations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()

                operations.append(operations_item)

        latest_sync_job_created_at = self.latest_sync_job_created_at
        latest_sync_job_status: Union[Unset, str] = UNSET
        if not isinstance(self.latest_sync_job_status, Unset):
            latest_sync_job_status = self.latest_sync_job_status.value

        resource_requirements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resource_requirements, Unset):
            resource_requirements = self.resource_requirements.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
                "name": name,
                "sourceId": source_id,
                "destinationId": destination_id,
                "syncCatalog": sync_catalog,
                "status": status,
                "source": source,
                "destination": destination,
                "isSyncing": is_syncing,
            }
        )
        if namespace_definition is not UNSET:
            field_dict["namespaceDefinition"] = namespace_definition
        if namespace_format is not UNSET:
            field_dict["namespaceFormat"] = namespace_format
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if operation_ids is not UNSET:
            field_dict["operationIds"] = operation_ids
        if operations is not UNSET:
            field_dict["operations"] = operations
        if latest_sync_job_created_at is not UNSET:
            field_dict["latestSyncJobCreatedAt"] = latest_sync_job_created_at
        if latest_sync_job_status is not UNSET:
            field_dict["latestSyncJobStatus"] = latest_sync_job_status
        if resource_requirements is not UNSET:
            field_dict["resourceRequirements"] = resource_requirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        name = d.pop("name")

        source_id = d.pop("sourceId")

        destination_id = d.pop("destinationId")

        sync_catalog = AirbyteCatalog.from_dict(d.pop("syncCatalog"))

        status = ConnectionStatus(d.pop("status"))

        source = SourceRead.from_dict(d.pop("source"))

        destination = DestinationRead.from_dict(d.pop("destination"))

        is_syncing = d.pop("isSyncing")

        _namespace_definition = d.pop("namespaceDefinition", UNSET)
        namespace_definition: Union[Unset, NamespaceDefinitionType]
        if isinstance(_namespace_definition, Unset):
            namespace_definition = UNSET
        else:
            namespace_definition = NamespaceDefinitionType(_namespace_definition)

        namespace_format = d.pop("namespaceFormat", UNSET)

        prefix = d.pop("prefix", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, ConnectionSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = ConnectionSchedule.from_dict(_schedule)

        operation_ids = cast(List[str], d.pop("operationIds", UNSET))

        operations = []
        _operations = d.pop("operations", UNSET)
        for operations_item_data in _operations or []:
            operations_item = OperationRead.from_dict(operations_item_data)

            operations.append(operations_item)

        latest_sync_job_created_at = d.pop("latestSyncJobCreatedAt", UNSET)

        _latest_sync_job_status = d.pop("latestSyncJobStatus", UNSET)
        latest_sync_job_status: Union[Unset, JobStatus]
        if isinstance(_latest_sync_job_status, Unset):
            latest_sync_job_status = UNSET
        else:
            latest_sync_job_status = JobStatus(_latest_sync_job_status)

        _resource_requirements = d.pop("resourceRequirements", UNSET)
        resource_requirements: Union[Unset, ResourceRequirements]
        if isinstance(_resource_requirements, Unset):
            resource_requirements = UNSET
        else:
            resource_requirements = ResourceRequirements.from_dict(_resource_requirements)

        web_backend_connection_read = cls(
            connection_id=connection_id,
            name=name,
            source_id=source_id,
            destination_id=destination_id,
            sync_catalog=sync_catalog,
            status=status,
            source=source,
            destination=destination,
            is_syncing=is_syncing,
            namespace_definition=namespace_definition,
            namespace_format=namespace_format,
            prefix=prefix,
            schedule=schedule,
            operation_ids=operation_ids,
            operations=operations,
            latest_sync_job_created_at=latest_sync_job_created_at,
            latest_sync_job_status=latest_sync_job_status,
            resource_requirements=resource_requirements,
        )

        web_backend_connection_read.additional_properties = d
        return web_backend_connection_read

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
