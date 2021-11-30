from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.operation_read import OperationRead

T = TypeVar("T", bound="OperationReadList")


@attr.s(auto_attribs=True)
class OperationReadList:
    """ """

    operations: List[OperationRead]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operations": operations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:
            operations_item = OperationRead.from_dict(operations_item_data)

            operations.append(operations_item)

        operation_read_list = cls(
            operations=operations,
        )

        operation_read_list.additional_properties = d
        return operation_read_list

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
