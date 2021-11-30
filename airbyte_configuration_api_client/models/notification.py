from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification_type import NotificationType
from ..models.slack_notification_configuration import SlackNotificationConfiguration
from ..types import UNSET, Unset

T = TypeVar("T", bound="Notification")


@attr.s(auto_attribs=True)
class Notification:
    """ """

    notification_type: NotificationType
    send_on_success: bool = False
    send_on_failure: bool = True
    slack_configuration: Union[Unset, SlackNotificationConfiguration] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notification_type = self.notification_type.value

        send_on_success = self.send_on_success
        send_on_failure = self.send_on_failure
        slack_configuration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.slack_configuration, Unset):
            slack_configuration = self.slack_configuration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notificationType": notification_type,
                "sendOnSuccess": send_on_success,
                "sendOnFailure": send_on_failure,
            }
        )
        if slack_configuration is not UNSET:
            field_dict["slackConfiguration"] = slack_configuration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notification_type = NotificationType(d.pop("notificationType"))

        send_on_success = d.pop("sendOnSuccess")

        send_on_failure = d.pop("sendOnFailure")

        _slack_configuration = d.pop("slackConfiguration", UNSET)
        slack_configuration: Union[Unset, SlackNotificationConfiguration]
        if isinstance(_slack_configuration, Unset):
            slack_configuration = UNSET
        else:
            slack_configuration = SlackNotificationConfiguration.from_dict(_slack_configuration)

        notification = cls(
            notification_type=notification_type,
            send_on_success=send_on_success,
            send_on_failure=send_on_failure,
            slack_configuration=slack_configuration,
        )

        notification.additional_properties = d
        return notification

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
