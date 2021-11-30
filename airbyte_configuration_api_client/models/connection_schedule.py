from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.connection_schedule_time_unit import ConnectionScheduleTimeUnit

T = TypeVar("T", bound="ConnectionSchedule")


@attr.s(auto_attribs=True)
class ConnectionSchedule:
    """if null, then no schedule is set."""

    units: int
    time_unit: ConnectionScheduleTimeUnit
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        units = self.units
        time_unit = self.time_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "units": units,
                "timeUnit": time_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        units = d.pop("units")

        time_unit = ConnectionScheduleTimeUnit(d.pop("timeUnit"))

        connection_schedule = cls(
            units=units,
            time_unit=time_unit,
        )

        connection_schedule.additional_properties = d
        return connection_schedule

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
