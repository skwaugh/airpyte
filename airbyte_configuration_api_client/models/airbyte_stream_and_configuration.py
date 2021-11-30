from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.airbyte_stream import AirbyteStream
from ..models.airbyte_stream_configuration import AirbyteStreamConfiguration
from ..types import UNSET, Unset

T = TypeVar("T", bound="AirbyteStreamAndConfiguration")


@attr.s(auto_attribs=True)
class AirbyteStreamAndConfiguration:
    """each stream is split in two parts; the immutable schema from source and mutable configuration for destination"""

    stream: Union[Unset, AirbyteStream] = UNSET
    config: Union[Unset, AirbyteStreamConfiguration] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stream, Unset):
            stream = self.stream.to_dict()

        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if stream is not UNSET:
            field_dict["stream"] = stream
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _stream = d.pop("stream", UNSET)
        stream: Union[Unset, AirbyteStream]
        if isinstance(_stream, Unset):
            stream = UNSET
        else:
            stream = AirbyteStream.from_dict(_stream)

        _config = d.pop("config", UNSET)
        config: Union[Unset, AirbyteStreamConfiguration]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = AirbyteStreamConfiguration.from_dict(_config)

        airbyte_stream_and_configuration = cls(
            stream=stream,
            config=config,
        )

        return airbyte_stream_and_configuration
