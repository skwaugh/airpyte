from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.source_read import SourceRead

T = TypeVar("T", bound="SourceReadList")


@attr.s(auto_attribs=True)
class SourceReadList:
    """ """

    sources: List[SourceRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()

            sources.append(sources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceRead.from_dict(sources_item_data)

            sources.append(sources_item)

        source_read_list = cls(
            sources=sources,
        )

        source_read_list.additional_properties = d
        return source_read_list

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
