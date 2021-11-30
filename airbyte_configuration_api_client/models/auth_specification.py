from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.auth_specification_auth_type import AuthSpecificationAuthType
from ..models.o_auth_2_specification import OAuth2Specification
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthSpecification")


@attr.s(auto_attribs=True)
class AuthSpecification:
    """ """

    auth_type: Union[Unset, AuthSpecificationAuthType] = UNSET
    oauth_2_specification: Union[Unset, OAuth2Specification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        oauth_2_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oauth_2_specification, Unset):
            oauth_2_specification = self.oauth_2_specification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if oauth_2_specification is not UNSET:
            field_dict["oauth2Specification"] = oauth_2_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _auth_type = d.pop("auth_type", UNSET)
        auth_type: Union[Unset, AuthSpecificationAuthType]
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = AuthSpecificationAuthType(_auth_type)

        _oauth_2_specification = d.pop("oauth2Specification", UNSET)
        oauth_2_specification: Union[Unset, OAuth2Specification]
        if isinstance(_oauth_2_specification, Unset):
            oauth_2_specification = UNSET
        else:
            oauth_2_specification = OAuth2Specification.from_dict(_oauth_2_specification)

        auth_specification = cls(
            auth_type=auth_type,
            oauth_2_specification=oauth_2_specification,
        )

        auth_specification.additional_properties = d
        return auth_specification

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
