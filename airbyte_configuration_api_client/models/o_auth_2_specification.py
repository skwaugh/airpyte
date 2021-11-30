from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="OAuth2Specification")


@attr.s(auto_attribs=True)
class OAuth2Specification:
    """An object containing any metadata needed to describe this connector's Oauth flow"""

    root_object: List[None]
    oauth_flow_init_parameters: List[List[str]]
    oauth_flow_output_parameters: List[List[str]]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        root_object = []
        for root_object_item_data in self.root_object:
            root_object_item = None

            root_object.append(root_object_item)

        oauth_flow_init_parameters = []
        for oauth_flow_init_parameters_item_data in self.oauth_flow_init_parameters:
            oauth_flow_init_parameters_item = oauth_flow_init_parameters_item_data

            oauth_flow_init_parameters.append(oauth_flow_init_parameters_item)

        oauth_flow_output_parameters = []
        for oauth_flow_output_parameters_item_data in self.oauth_flow_output_parameters:
            oauth_flow_output_parameters_item = oauth_flow_output_parameters_item_data

            oauth_flow_output_parameters.append(oauth_flow_output_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rootObject": root_object,
                "oauthFlowInitParameters": oauth_flow_init_parameters,
                "oauthFlowOutputParameters": oauth_flow_output_parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        root_object = []
        _root_object = d.pop("rootObject")
        for root_object_item_data in _root_object:
            root_object_item = None

            root_object.append(root_object_item)

        oauth_flow_init_parameters = []
        _oauth_flow_init_parameters = d.pop("oauthFlowInitParameters")
        for oauth_flow_init_parameters_item_data in _oauth_flow_init_parameters:
            oauth_flow_init_parameters_item = cast(List[str], oauth_flow_init_parameters_item_data)

            oauth_flow_init_parameters.append(oauth_flow_init_parameters_item)

        oauth_flow_output_parameters = []
        _oauth_flow_output_parameters = d.pop("oauthFlowOutputParameters")
        for oauth_flow_output_parameters_item_data in _oauth_flow_output_parameters:
            oauth_flow_output_parameters_item = cast(List[str], oauth_flow_output_parameters_item_data)

            oauth_flow_output_parameters.append(oauth_flow_output_parameters_item)

        o_auth_2_specification = cls(
            root_object=root_object,
            oauth_flow_init_parameters=oauth_flow_init_parameters,
            oauth_flow_output_parameters=oauth_flow_output_parameters,
        )

        o_auth_2_specification.additional_properties = d
        return o_auth_2_specification

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
