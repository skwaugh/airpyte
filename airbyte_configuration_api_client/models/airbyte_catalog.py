from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.airbyte_stream_and_configuration import AirbyteStreamAndConfiguration

T = TypeVar("T", bound="AirbyteCatalog")


@attr.s(auto_attribs=True)
class AirbyteCatalog:
    """describes the available schema (catalog)."""

    streams: List[AirbyteStreamAndConfiguration]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        streams = []
        for streams_item_data in self.streams:
            streams_item = streams_item_data.to_dict()

            streams.append(streams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "streams": streams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        streams = []
        _streams = d.pop("streams")
        for streams_item_data in _streams:
            streams_item = AirbyteStreamAndConfiguration.from_dict(streams_item_data)

            streams.append(streams_item)

        airbyte_catalog = cls(
            streams=streams,
        )

        airbyte_catalog.additional_properties = d
        return airbyte_catalog

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
