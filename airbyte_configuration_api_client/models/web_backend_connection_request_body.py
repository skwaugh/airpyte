from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebBackendConnectionRequestBody")


@attr.s(auto_attribs=True)
class WebBackendConnectionRequestBody:
    """ """

    connection_id: str
    with_refreshed_catalog: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        with_refreshed_catalog = self.with_refreshed_catalog

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionId": connection_id,
            }
        )
        if with_refreshed_catalog is not UNSET:
            field_dict["withRefreshedCatalog"] = with_refreshed_catalog

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connectionId")

        with_refreshed_catalog = d.pop("withRefreshedCatalog", UNSET)

        web_backend_connection_request_body = cls(
            connection_id=connection_id,
            with_refreshed_catalog=with_refreshed_catalog,
        )

        web_backend_connection_request_body.additional_properties = d
        return web_backend_connection_request_body

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
