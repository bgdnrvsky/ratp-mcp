from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar_exception import CalendarException
    from ..models.calendar_period import CalendarPeriod
    from ..models.validity_pattern import ValidityPattern
    from ..models.week_pattern import WeekPattern


T = TypeVar("T", bound="Calendar")


@_attrs_define
class Calendar:
    """
    Attributes:
        active_periods (list[CalendarPeriod] | Unset):
        name (str | Unset): Name of the object
        validity_pattern (ValidityPattern | Unset):
        exceptions (list[CalendarException] | Unset):
        week_pattern (WeekPattern | Unset):
        id (str | Unset): Identifier of the object
    """

    active_periods: list[CalendarPeriod] | Unset = UNSET
    name: str | Unset = UNSET
    validity_pattern: ValidityPattern | Unset = UNSET
    exceptions: list[CalendarException] | Unset = UNSET
    week_pattern: WeekPattern | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_periods, Unset):
            active_periods = []
            for active_periods_item_data in self.active_periods:
                active_periods_item = active_periods_item_data.to_dict()
                active_periods.append(active_periods_item)

        name = self.name

        validity_pattern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validity_pattern, Unset):
            validity_pattern = self.validity_pattern.to_dict()

        exceptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exceptions, Unset):
            exceptions = []
            for exceptions_item_data in self.exceptions:
                exceptions_item = exceptions_item_data.to_dict()
                exceptions.append(exceptions_item)

        week_pattern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.week_pattern, Unset):
            week_pattern = self.week_pattern.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_periods is not UNSET:
            field_dict["active_periods"] = active_periods
        if name is not UNSET:
            field_dict["name"] = name
        if validity_pattern is not UNSET:
            field_dict["validity_pattern"] = validity_pattern
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if week_pattern is not UNSET:
            field_dict["week_pattern"] = week_pattern
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_exception import CalendarException
        from ..models.calendar_period import CalendarPeriod
        from ..models.validity_pattern import ValidityPattern
        from ..models.week_pattern import WeekPattern

        d = dict(src_dict)
        _active_periods = d.pop("active_periods", UNSET)
        active_periods: list[CalendarPeriod] | Unset = UNSET
        if _active_periods is not UNSET:
            active_periods = []
            for active_periods_item_data in _active_periods:
                active_periods_item = CalendarPeriod.from_dict(active_periods_item_data)

                active_periods.append(active_periods_item)

        name = d.pop("name", UNSET)

        _validity_pattern = d.pop("validity_pattern", UNSET)
        validity_pattern: ValidityPattern | Unset
        if isinstance(_validity_pattern, Unset):
            validity_pattern = UNSET
        else:
            validity_pattern = ValidityPattern.from_dict(_validity_pattern)

        _exceptions = d.pop("exceptions", UNSET)
        exceptions: list[CalendarException] | Unset = UNSET
        if _exceptions is not UNSET:
            exceptions = []
            for exceptions_item_data in _exceptions:
                exceptions_item = CalendarException.from_dict(exceptions_item_data)

                exceptions.append(exceptions_item)

        _week_pattern = d.pop("week_pattern", UNSET)
        week_pattern: WeekPattern | Unset
        if isinstance(_week_pattern, Unset):
            week_pattern = UNSET
        else:
            week_pattern = WeekPattern.from_dict(_week_pattern)

        id = d.pop("id", UNSET)

        calendar = cls(
            active_periods=active_periods,
            name=name,
            validity_pattern=validity_pattern,
            exceptions=exceptions,
            week_pattern=week_pattern,
            id=id,
        )

        calendar.additional_properties = d
        return calendar

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
