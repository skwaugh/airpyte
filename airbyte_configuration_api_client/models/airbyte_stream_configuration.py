from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.destination_sync_mode import DestinationSyncMode
from ..models.sync_mode import SyncMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AirbyteStreamConfiguration")


@attr.s(auto_attribs=True)
class AirbyteStreamConfiguration:
    """the mutable part of the stream to configure the destination"""

    sync_mode: SyncMode
    destination_sync_mode: DestinationSyncMode
    cursor_field: Union[Unset, List[str]] = UNSET
    primary_key: Union[Unset, List[List[str]]] = UNSET
    alias_name: Union[Unset, str] = UNSET
    selected: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sync_mode = self.sync_mode.value

        destination_sync_mode = self.destination_sync_mode.value

        cursor_field: Union[Unset, List[str]] = UNSET
        if not isinstance(self.cursor_field, Unset):
            cursor_field = self.cursor_field

        primary_key: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.primary_key, Unset):
            primary_key = []
            for primary_key_item_data in self.primary_key:
                primary_key_item = primary_key_item_data

                primary_key.append(primary_key_item)

        alias_name = self.alias_name
        selected = self.selected

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "syncMode": sync_mode,
                "destinationSyncMode": destination_sync_mode,
            }
        )
        if cursor_field is not UNSET:
            field_dict["cursorField"] = cursor_field
        if primary_key is not UNSET:
            field_dict["primaryKey"] = primary_key
        if alias_name is not UNSET:
            field_dict["aliasName"] = alias_name
        if selected is not UNSET:
            field_dict["selected"] = selected

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sync_mode = SyncMode(d.pop("syncMode"))

        destination_sync_mode = DestinationSyncMode(d.pop("destinationSyncMode"))

        cursor_field = cast(List[str], d.pop("cursorField", UNSET))

        primary_key = []
        _primary_key = d.pop("primaryKey", UNSET)
        for primary_key_item_data in _primary_key or []:
            primary_key_item = cast(List[str], primary_key_item_data)

            primary_key.append(primary_key_item)

        alias_name = d.pop("aliasName", UNSET)

        selected = d.pop("selected", UNSET)

        airbyte_stream_configuration = cls(
            sync_mode=sync_mode,
            destination_sync_mode=destination_sync_mode,
            cursor_field=cursor_field,
            primary_key=primary_key,
            alias_name=alias_name,
            selected=selected,
        )

        return airbyte_stream_configuration
