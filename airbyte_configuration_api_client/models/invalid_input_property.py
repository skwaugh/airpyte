from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidInputProperty")


@attr.s(auto_attribs=True)
class InvalidInputProperty:
    """ """

    property_path: str
    invalid_value: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_path = self.property_path
        invalid_value = self.invalid_value
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "propertyPath": property_path,
            }
        )
        if invalid_value is not UNSET:
            field_dict["invalidValue"] = invalid_value
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        property_path = d.pop("propertyPath")

        invalid_value = d.pop("invalidValue", UNSET)

        message = d.pop("message", UNSET)

        invalid_input_property = cls(
            property_path=property_path,
            invalid_value=invalid_value,
            message=message,
        )

        invalid_input_property.additional_properties = d
        return invalid_input_property

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
