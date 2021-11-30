from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.invalid_input_property import InvalidInputProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidInputExceptionInfo")


@attr.s(auto_attribs=True)
class InvalidInputExceptionInfo:
    """ """

    message: str
    validation_errors: List[InvalidInputProperty]
    exception_class_name: Union[Unset, str] = UNSET
    exception_stack: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        validation_errors = []
        for validation_errors_item_data in self.validation_errors:
            validation_errors_item = validation_errors_item_data.to_dict()

            validation_errors.append(validation_errors_item)

        exception_class_name = self.exception_class_name
        exception_stack: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exception_stack, Unset):
            exception_stack = self.exception_stack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "validationErrors": validation_errors,
            }
        )
        if exception_class_name is not UNSET:
            field_dict["exceptionClassName"] = exception_class_name
        if exception_stack is not UNSET:
            field_dict["exceptionStack"] = exception_stack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        validation_errors = []
        _validation_errors = d.pop("validationErrors")
        for validation_errors_item_data in _validation_errors:
            validation_errors_item = InvalidInputProperty.from_dict(validation_errors_item_data)

            validation_errors.append(validation_errors_item)

        exception_class_name = d.pop("exceptionClassName", UNSET)

        exception_stack = cast(List[str], d.pop("exceptionStack", UNSET))

        invalid_input_exception_info = cls(
            message=message,
            validation_errors=validation_errors,
            exception_class_name=exception_class_name,
            exception_stack=exception_stack,
        )

        invalid_input_exception_info.additional_properties = d
        return invalid_input_exception_info

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
