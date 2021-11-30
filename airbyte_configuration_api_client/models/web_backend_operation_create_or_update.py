from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.operator_configuration import OperatorConfiguration
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebBackendOperationCreateOrUpdate")


@attr.s(auto_attribs=True)
class WebBackendOperationCreateOrUpdate:
    """ """

    workspace_id: str
    name: str
    operator_configuration: OperatorConfiguration
    operation_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace_id = self.workspace_id
        name = self.name
        operator_configuration = self.operator_configuration.to_dict()

        operation_id = self.operation_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "name": name,
                "operatorConfiguration": operator_configuration,
            }
        )
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        operator_configuration = OperatorConfiguration.from_dict(d.pop("operatorConfiguration"))

        operation_id = d.pop("operationId", UNSET)

        web_backend_operation_create_or_update = cls(
            workspace_id=workspace_id,
            name=name,
            operator_configuration=operator_configuration,
            operation_id=operation_id,
        )

        web_backend_operation_create_or_update.additional_properties = d
        return web_backend_operation_create_or_update

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
