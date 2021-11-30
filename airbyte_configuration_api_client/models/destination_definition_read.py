from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DestinationDefinitionRead")


@attr.s(auto_attribs=True)
class DestinationDefinitionRead:
    """ """

    destination_definition_id: str
    name: str
    docker_repository: str
    docker_image_tag: str
    documentation_url: str
    icon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        destination_definition_id = self.destination_definition_id
        name = self.name
        docker_repository = self.docker_repository
        docker_image_tag = self.docker_image_tag
        documentation_url = self.documentation_url
        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationDefinitionId": destination_definition_id,
                "name": name,
                "dockerRepository": docker_repository,
                "dockerImageTag": docker_image_tag,
                "documentationUrl": documentation_url,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_definition_id = d.pop("destinationDefinitionId")

        name = d.pop("name")

        docker_repository = d.pop("dockerRepository")

        docker_image_tag = d.pop("dockerImageTag")

        documentation_url = d.pop("documentationUrl")

        icon = d.pop("icon", UNSET)

        destination_definition_read = cls(
            destination_definition_id=destination_definition_id,
            name=name,
            docker_repository=docker_repository,
            docker_image_tag=docker_image_tag,
            documentation_url=documentation_url,
            icon=icon,
        )

        destination_definition_read.additional_properties = d
        return destination_definition_read

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
