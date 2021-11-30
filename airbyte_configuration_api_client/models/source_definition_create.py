from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceDefinitionCreate")


@attr.s(auto_attribs=True)
class SourceDefinitionCreate:
    """ """

    name: str
    docker_repository: str
    docker_image_tag: str
    documentation_url: str
    icon: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        docker_repository = self.docker_repository
        docker_image_tag = self.docker_image_tag
        documentation_url = self.documentation_url
        icon = self.icon

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        name = d.pop("name")

        docker_repository = d.pop("dockerRepository")

        docker_image_tag = d.pop("dockerImageTag")

        documentation_url = d.pop("documentationUrl")

        icon = d.pop("icon", UNSET)

        source_definition_create = cls(
            name=name,
            docker_repository=docker_repository,
            docker_image_tag=docker_image_tag,
            documentation_url=documentation_url,
            icon=icon,
        )

        source_definition_create.additional_properties = d
        return source_definition_create

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
