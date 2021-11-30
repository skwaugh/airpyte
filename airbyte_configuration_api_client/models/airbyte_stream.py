from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.stream_json_schema import StreamJsonSchema
from ..models.sync_mode import SyncMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AirbyteStream")


@attr.s(auto_attribs=True)
class AirbyteStream:
    """the immutable schema defined by the source"""

    name: str
    json_schema: Union[Unset, StreamJsonSchema] = UNSET
    supported_sync_modes: Union[Unset, List[SyncMode]] = UNSET
    source_defined_cursor: Union[Unset, bool] = UNSET
    default_cursor_field: Union[Unset, List[str]] = UNSET
    source_defined_primary_key: Union[Unset, List[List[str]]] = UNSET
    namespace: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        json_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json_schema, Unset):
            json_schema = self.json_schema.to_dict()

        supported_sync_modes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.supported_sync_modes, Unset):
            supported_sync_modes = []
            for supported_sync_modes_item_data in self.supported_sync_modes:
                supported_sync_modes_item = supported_sync_modes_item_data.value

                supported_sync_modes.append(supported_sync_modes_item)

        source_defined_cursor = self.source_defined_cursor
        default_cursor_field: Union[Unset, List[str]] = UNSET
        if not isinstance(self.default_cursor_field, Unset):
            default_cursor_field = self.default_cursor_field

        source_defined_primary_key: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.source_defined_primary_key, Unset):
            source_defined_primary_key = []
            for source_defined_primary_key_item_data in self.source_defined_primary_key:
                source_defined_primary_key_item = source_defined_primary_key_item_data

                source_defined_primary_key.append(source_defined_primary_key_item)

        namespace = self.namespace

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if json_schema is not UNSET:
            field_dict["jsonSchema"] = json_schema
        if supported_sync_modes is not UNSET:
            field_dict["supportedSyncModes"] = supported_sync_modes
        if source_defined_cursor is not UNSET:
            field_dict["sourceDefinedCursor"] = source_defined_cursor
        if default_cursor_field is not UNSET:
            field_dict["defaultCursorField"] = default_cursor_field
        if source_defined_primary_key is not UNSET:
            field_dict["sourceDefinedPrimaryKey"] = source_defined_primary_key
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _json_schema = d.pop("jsonSchema", UNSET)
        json_schema: Union[Unset, StreamJsonSchema]
        if isinstance(_json_schema, Unset):
            json_schema = UNSET
        else:
            json_schema = StreamJsonSchema.from_dict(_json_schema)

        supported_sync_modes = []
        _supported_sync_modes = d.pop("supportedSyncModes", UNSET)
        for supported_sync_modes_item_data in _supported_sync_modes or []:
            supported_sync_modes_item = SyncMode(supported_sync_modes_item_data)

            supported_sync_modes.append(supported_sync_modes_item)

        source_defined_cursor = d.pop("sourceDefinedCursor", UNSET)

        default_cursor_field = cast(List[str], d.pop("defaultCursorField", UNSET))

        source_defined_primary_key = []
        _source_defined_primary_key = d.pop("sourceDefinedPrimaryKey", UNSET)
        for source_defined_primary_key_item_data in _source_defined_primary_key or []:
            source_defined_primary_key_item = cast(List[str], source_defined_primary_key_item_data)

            source_defined_primary_key.append(source_defined_primary_key_item)

        namespace = d.pop("namespace", UNSET)

        airbyte_stream = cls(
            name=name,
            json_schema=json_schema,
            supported_sync_modes=supported_sync_modes,
            source_defined_cursor=source_defined_cursor,
            default_cursor_field=default_cursor_field,
            source_defined_primary_key=source_defined_primary_key,
            namespace=namespace,
        )

        return airbyte_stream
