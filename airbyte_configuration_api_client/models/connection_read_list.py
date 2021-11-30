from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.connection_read import ConnectionRead

T = TypeVar("T", bound="ConnectionReadList")


@attr.s(auto_attribs=True)
class ConnectionReadList:
    """ """

    connections: List[ConnectionRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()

            connections.append(connections_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connections": connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = ConnectionRead.from_dict(connections_item_data)

            connections.append(connections_item)

        connection_read_list = cls(
            connections=connections,
        )

        connection_read_list.additional_properties = d
        return connection_read_list

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
