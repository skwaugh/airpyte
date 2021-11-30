from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthConfigSpecification")


@attr.s(auto_attribs=True)
class OAuthConfigSpecification:
    """ """

    oauth_user_input_from_connector_config_specification: Union[Unset, None] = UNSET
    complete_o_auth_output_specification: Union[Unset, None] = UNSET
    complete_o_auth_server_input_specification: Union[Unset, None] = UNSET
    complete_o_auth_server_output_specification: Union[Unset, None] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        oauth_user_input_from_connector_config_specification = None

        complete_o_auth_output_specification = None

        complete_o_auth_server_input_specification = None

        complete_o_auth_server_output_specification = None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oauth_user_input_from_connector_config_specification is not UNSET:
            field_dict[
                "oauthUserInputFromConnectorConfigSpecification"
            ] = oauth_user_input_from_connector_config_specification
        if complete_o_auth_output_specification is not UNSET:
            field_dict["completeOAuthOutputSpecification"] = complete_o_auth_output_specification
        if complete_o_auth_server_input_specification is not UNSET:
            field_dict["completeOAuthServerInputSpecification"] = complete_o_auth_server_input_specification
        if complete_o_auth_server_output_specification is not UNSET:
            field_dict["completeOAuthServerOutputSpecification"] = complete_o_auth_server_output_specification

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        oauth_user_input_from_connector_config_specification = None

        complete_o_auth_output_specification = None

        complete_o_auth_server_input_specification = None

        complete_o_auth_server_output_specification = None

        o_auth_config_specification = cls(
            oauth_user_input_from_connector_config_specification=oauth_user_input_from_connector_config_specification,
            complete_o_auth_output_specification=complete_o_auth_output_specification,
            complete_o_auth_server_input_specification=complete_o_auth_server_input_specification,
            complete_o_auth_server_output_specification=complete_o_auth_server_output_specification,
        )

        o_auth_config_specification.additional_properties = d
        return o_auth_config_specification

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
