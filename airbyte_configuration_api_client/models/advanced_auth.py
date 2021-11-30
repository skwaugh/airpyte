from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.advanced_auth_auth_flow_type import AdvancedAuthAuthFlowType
from ..models.o_auth_config_specification import OAuthConfigSpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvancedAuth")


@attr.s(auto_attribs=True)
class AdvancedAuth:
    """ """

    auth_flow_type: Union[Unset, AdvancedAuthAuthFlowType] = UNSET
    predicate_key: Union[Unset, List[str]] = UNSET
    predicate_value: Union[Unset, str] = UNSET
    oauth_config_specification: Union[Unset, OAuthConfigSpecification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_flow_type: Union[Unset, str] = UNSET
        if not isinstance(self.auth_flow_type, Unset):
            auth_flow_type = self.auth_flow_type.value

        predicate_key: Union[Unset, List[str]] = UNSET
        if not isinstance(self.predicate_key, Unset):
            predicate_key = self.predicate_key

        predicate_value = self.predicate_value
        oauth_config_specification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oauth_config_specification, Unset):
            oauth_config_specification = self.oauth_config_specification.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_flow_type is not UNSET:
            field_dict["authFlowType"] = auth_flow_type
        if predicate_key is not UNSET:
            field_dict["predicateKey"] = predicate_key
        if predicate_value is not UNSET:
            field_dict["predicateValue"] = predicate_value
        if oauth_config_specification is not UNSET:
            field_dict["oauthConfigSpecification"] = oauth_config_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _auth_flow_type = d.pop("authFlowType", UNSET)
        auth_flow_type: Union[Unset, AdvancedAuthAuthFlowType]
        if isinstance(_auth_flow_type, Unset):
            auth_flow_type = UNSET
        else:
            auth_flow_type = AdvancedAuthAuthFlowType(_auth_flow_type)

        predicate_key = cast(List[str], d.pop("predicateKey", UNSET))

        predicate_value = d.pop("predicateValue", UNSET)

        _oauth_config_specification = d.pop("oauthConfigSpecification", UNSET)
        oauth_config_specification: Union[Unset, OAuthConfigSpecification]
        if isinstance(_oauth_config_specification, Unset):
            oauth_config_specification = UNSET
        else:
            oauth_config_specification = OAuthConfigSpecification.from_dict(_oauth_config_specification)

        advanced_auth = cls(
            auth_flow_type=auth_flow_type,
            predicate_key=predicate_key,
            predicate_value=predicate_value,
            oauth_config_specification=oauth_config_specification,
        )

        advanced_auth.additional_properties = d
        return advanced_auth

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
