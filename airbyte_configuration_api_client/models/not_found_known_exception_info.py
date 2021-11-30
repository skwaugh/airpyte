from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotFoundKnownExceptionInfo")


@attr.s(auto_attribs=True)
class NotFoundKnownExceptionInfo:
    """ """

    message: str
    id: Union[Unset, str] = UNSET
    exception_class_name: Union[Unset, str] = UNSET
    exception_stack: Union[Unset, List[str]] = UNSET
    root_cause_exception_class_name: Union[Unset, str] = UNSET
    root_cause_exception_stack: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        id = self.id
        exception_class_name = self.exception_class_name
        exception_stack: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exception_stack, Unset):
            exception_stack = self.exception_stack

        root_cause_exception_class_name = self.root_cause_exception_class_name
        root_cause_exception_stack: Union[Unset, List[str]] = UNSET
        if not isinstance(self.root_cause_exception_stack, Unset):
            root_cause_exception_stack = self.root_cause_exception_stack

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if exception_class_name is not UNSET:
            field_dict["exceptionClassName"] = exception_class_name
        if exception_stack is not UNSET:
            field_dict["exceptionStack"] = exception_stack
        if root_cause_exception_class_name is not UNSET:
            field_dict["rootCauseExceptionClassName"] = root_cause_exception_class_name
        if root_cause_exception_stack is not UNSET:
            field_dict["rootCauseExceptionStack"] = root_cause_exception_stack

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        id = d.pop("id", UNSET)

        exception_class_name = d.pop("exceptionClassName", UNSET)

        exception_stack = cast(List[str], d.pop("exceptionStack", UNSET))

        root_cause_exception_class_name = d.pop("rootCauseExceptionClassName", UNSET)

        root_cause_exception_stack = cast(List[str], d.pop("rootCauseExceptionStack", UNSET))

        not_found_known_exception_info = cls(
            message=message,
            id=id,
            exception_class_name=exception_class_name,
            exception_stack=exception_stack,
            root_cause_exception_class_name=root_cause_exception_class_name,
            root_cause_exception_stack=root_cause_exception_stack,
        )

        not_found_known_exception_info.additional_properties = d
        return not_found_known_exception_info

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
