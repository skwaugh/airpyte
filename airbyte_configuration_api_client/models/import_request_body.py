from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ImportRequestBody")


@attr.s(auto_attribs=True)
class ImportRequestBody:
    """ """

    resource_id: str
    workspace_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_id = self.resource_id
        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "workspaceId": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_id = d.pop("resourceId")

        workspace_id = d.pop("workspaceId")

        import_request_body = cls(
            resource_id=resource_id,
            workspace_id=workspace_id,
        )

        import_request_body.additional_properties = d
        return import_request_body

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
