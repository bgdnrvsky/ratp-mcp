from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_time_type import DateTimeType
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="Row")


@_attrs_define
class Row:
    """
    Attributes:
        date_times (list[DateTimeType]):
        stop_point (StopPoint | Unset):
    """

    date_times: list[DateTimeType]
    stop_point: StopPoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_times = []
        for date_times_item_data in self.date_times:
            date_times_item = date_times_item_data.to_dict()
            date_times.append(date_times_item)

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_times": date_times,
            }
        )
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_time_type import DateTimeType
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        date_times = []
        _date_times = d.pop("date_times")
        for date_times_item_data in _date_times:
            date_times_item = DateTimeType.from_dict(date_times_item_data)

            date_times.append(date_times_item)

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        row = cls(
            date_times=date_times,
            stop_point=stop_point,
        )

        row.additional_properties = d
        return row

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
