from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SourceDefinitionUpdate")


@attr.s(auto_attribs=True)
class SourceDefinitionUpdate:
    """Update the SourceDefinition. Currently, the only allowed attribute to update is the default docker image version."""

    source_definition_id: str
    docker_image_tag: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_definition_id = self.source_definition_id
        docker_image_tag = self.docker_image_tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceDefinitionId": source_definition_id,
                "dockerImageTag": docker_image_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_definition_id = d.pop("sourceDefinitionId")

        docker_image_tag = d.pop("dockerImageTag")

        source_definition_update = cls(
            source_definition_id=source_definition_id,
            docker_image_tag=docker_image_tag,
        )

        source_definition_update.additional_properties = d
        return source_definition_update

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
