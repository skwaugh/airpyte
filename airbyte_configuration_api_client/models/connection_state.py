from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_state_object import ConnectionStateObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionState")


@attr.s(auto_attribs=True)
class ConnectionState:
    """ """

    connection_id: str
    state: Union[Unset, ConnectionStateObject] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        _state = d.pop("state", UNSET)
        state: Union[Unset, ConnectionStateObject]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ConnectionStateObject.from_dict(_state)

        connection_state = cls(
            connection_id=connection_id,
            state=state,
        )

        connection_state.additional_properties = d
        return connection_state

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
