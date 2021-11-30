from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.operator_normalization_option import OperatorNormalizationOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorNormalization")


@attr.s(auto_attribs=True)
class OperatorNormalization:
    """ """

    option: Union[Unset, OperatorNormalizationOption] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        option: Union[Unset, str] = UNSET
        if not isinstance(self.option, Unset):
            option = self.option.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option is not UNSET:
            field_dict["option"] = option

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _option = d.pop("option", UNSET)
        option: Union[Unset, OperatorNormalizationOption]
        if isinstance(_option, Unset):
            option = UNSET
        else:
            option = OperatorNormalizationOption(_option)

        operator_normalization = cls(
            option=option,
        )

        operator_normalization.additional_properties = d
        return operator_normalization

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
