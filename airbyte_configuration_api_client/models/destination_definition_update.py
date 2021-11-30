from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DestinationDefinitionUpdate")


@attr.s(auto_attribs=True)
class DestinationDefinitionUpdate:
    """ """

    destination_definition_id: str
    docker_image_tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination_definition_id = self.destination_definition_id
        docker_image_tag = self.docker_image_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationDefinitionId": destination_definition_id,
            }
        )
        if docker_image_tag is not UNSET:
            field_dict["dockerImageTag"] = docker_image_tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_definition_id = d.pop("destinationDefinitionId")

        docker_image_tag = d.pop("dockerImageTag", UNSET)

        destination_definition_update = cls(
            destination_definition_id=destination_definition_id,
            docker_image_tag=docker_image_tag,
        )

        destination_definition_update.additional_properties = d
        return destination_definition_update

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
