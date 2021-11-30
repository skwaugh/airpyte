from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="OAuthConsentRead")


@attr.s(auto_attribs=True)
class OAuthConsentRead:
    """ """

    consent_url: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consent_url = self.consent_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consentUrl": consent_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        consent_url = d.pop("consentUrl")

        o_auth_consent_read = cls(
            consent_url=consent_url,
        )

        o_auth_consent_read.additional_properties = d
        return o_auth_consent_read

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
