from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification import Notification
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceCreate")


@attr.s(auto_attribs=True)
class WorkspaceCreate:
    """ """

    name: str
    email: Union[Unset, str] = UNSET
    anonymous_data_collection: Union[Unset, bool] = UNSET
    news: Union[Unset, bool] = UNSET
    security_updates: Union[Unset, bool] = UNSET
    notifications: Union[Unset, List[Notification]] = UNSET
    display_setup_wizard: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        email = self.email
        anonymous_data_collection = self.anonymous_data_collection
        news = self.news
        security_updates = self.security_updates
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()

                notifications.append(notifications_item)

        display_setup_wizard = self.display_setup_wizard

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if anonymous_data_collection is not UNSET:
            field_dict["anonymousDataCollection"] = anonymous_data_collection
        if news is not UNSET:
            field_dict["news"] = news
        if security_updates is not UNSET:
            field_dict["securityUpdates"] = security_updates
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if display_setup_wizard is not UNSET:
            field_dict["displaySetupWizard"] = display_setup_wizard

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        email = d.pop("email", UNSET)

        anonymous_data_collection = d.pop("anonymousDataCollection", UNSET)

        news = d.pop("news", UNSET)

        security_updates = d.pop("securityUpdates", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = Notification.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        display_setup_wizard = d.pop("displaySetupWizard", UNSET)

        workspace_create = cls(
            name=name,
            email=email,
            anonymous_data_collection=anonymous_data_collection,
            news=news,
            security_updates=security_updates,
            notifications=notifications,
            display_setup_wizard=display_setup_wizard,
        )

        workspace_create.additional_properties = d
        return workspace_create

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
