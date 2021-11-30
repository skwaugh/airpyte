from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification import Notification
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceRead")


@attr.s(auto_attribs=True)
class WorkspaceRead:
    """ """

    workspace_id: str
    customer_id: str
    name: str
    slug: str
    initial_setup_complete: bool
    email: Union[Unset, str] = UNSET
    display_setup_wizard: Union[Unset, bool] = UNSET
    anonymous_data_collection: Union[Unset, bool] = UNSET
    news: Union[Unset, bool] = UNSET
    security_updates: Union[Unset, bool] = UNSET
    notifications: Union[Unset, List[Notification]] = UNSET
    first_completed_sync: Union[Unset, bool] = UNSET
    feedback_done: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        workspace_id = self.workspace_id
        customer_id = self.customer_id
        name = self.name
        slug = self.slug
        initial_setup_complete = self.initial_setup_complete
        email = self.email
        display_setup_wizard = self.display_setup_wizard
        anonymous_data_collection = self.anonymous_data_collection
        news = self.news
        security_updates = self.security_updates
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.to_dict()

                notifications.append(notifications_item)

        first_completed_sync = self.first_completed_sync
        feedback_done = self.feedback_done

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspaceId": workspace_id,
                "customerId": customer_id,
                "name": name,
                "slug": slug,
                "initialSetupComplete": initial_setup_complete,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if display_setup_wizard is not UNSET:
            field_dict["displaySetupWizard"] = display_setup_wizard
        if anonymous_data_collection is not UNSET:
            field_dict["anonymousDataCollection"] = anonymous_data_collection
        if news is not UNSET:
            field_dict["news"] = news
        if security_updates is not UNSET:
            field_dict["securityUpdates"] = security_updates
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if first_completed_sync is not UNSET:
            field_dict["firstCompletedSync"] = first_completed_sync
        if feedback_done is not UNSET:
            field_dict["feedbackDone"] = feedback_done

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        workspace_id = d.pop("workspaceId")

        customer_id = d.pop("customerId")

        name = d.pop("name")

        slug = d.pop("slug")

        initial_setup_complete = d.pop("initialSetupComplete")

        email = d.pop("email", UNSET)

        display_setup_wizard = d.pop("displaySetupWizard", UNSET)

        anonymous_data_collection = d.pop("anonymousDataCollection", UNSET)

        news = d.pop("news", UNSET)

        security_updates = d.pop("securityUpdates", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = Notification.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        first_completed_sync = d.pop("firstCompletedSync", UNSET)

        feedback_done = d.pop("feedbackDone", UNSET)

        workspace_read = cls(
            workspace_id=workspace_id,
            customer_id=customer_id,
            name=name,
            slug=slug,
            initial_setup_complete=initial_setup_complete,
            email=email,
            display_setup_wizard=display_setup_wizard,
            anonymous_data_collection=anonymous_data_collection,
            news=news,
            security_updates=security_updates,
            notifications=notifications,
            first_completed_sync=first_completed_sync,
            feedback_done=feedback_done,
        )

        workspace_read.additional_properties = d
        return workspace_read

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
