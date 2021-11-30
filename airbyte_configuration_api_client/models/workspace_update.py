from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification import Notification
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceUpdate")


@attr.s(auto_attribs=True)
class WorkspaceUpdate:
    """ """

    workspace_id: str
    initial_setup_complete: bool
    anonymous_data_collection: bool
    news: bool
    security_updates: bool
    email: Union[Unset, str] = UNSET
    display_setup_wizard: Union[Unset, bool] = UNSET
    notifications: Union[Unset, List[Notification]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace_id = self.workspace_id
        initial_setup_complete = self.initial_setup_complete
        anonymous_data_collection = self.anonymous_data_collection
        news = self.news
        security_updates = self.security_updates
        email = self.email
        display_setup_wizard = self.display_setup_wizard
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()

                notifications.append(notifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "initialSetupComplete": initial_setup_complete,
                "anonymousDataCollection": anonymous_data_collection,
                "news": news,
                "securityUpdates": security_updates,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if display_setup_wizard is not UNSET:
            field_dict["displaySetupWizard"] = display_setup_wizard
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_id = d.pop("workspaceId")

        initial_setup_complete = d.pop("initialSetupComplete")

        anonymous_data_collection = d.pop("anonymousDataCollection")

        news = d.pop("news")

        security_updates = d.pop("securityUpdates")

        email = d.pop("email", UNSET)

        display_setup_wizard = d.pop("displaySetupWizard", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = Notification.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        workspace_update = cls(
            workspace_id=workspace_id,
            initial_setup_complete=initial_setup_complete,
            anonymous_data_collection=anonymous_data_collection,
            news=news,
            security_updates=security_updates,
            email=email,
            display_setup_wizard=display_setup_wizard,
            notifications=notifications,
        )

        workspace_update.additional_properties = d
        return workspace_update

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
