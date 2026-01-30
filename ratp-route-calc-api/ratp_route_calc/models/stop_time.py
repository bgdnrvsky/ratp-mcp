from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.journey_pattern_point import JourneyPatternPoint
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="StopTime")


@_attrs_define
class StopTime:
    stop_point: StopPoint | Unset = UNSET
    utc_arrival_time: str | Unset = UNSET
    utc_departure_time: str | Unset = UNSET
    headsign: str | Unset = UNSET
    arrival_time: str | Unset = UNSET
    journey_pattern_point: JourneyPatternPoint | Unset = UNSET
    departure_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        utc_arrival_time = self.utc_arrival_time

        utc_departure_time = self.utc_departure_time

        headsign = self.headsign

        arrival_time = self.arrival_time

        journey_pattern_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.journey_pattern_point, Unset):
            journey_pattern_point = self.journey_pattern_point.to_dict()

        departure_time = self.departure_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if utc_arrival_time is not UNSET:
            field_dict["utc_arrival_time"] = utc_arrival_time
        if utc_departure_time is not UNSET:
            field_dict["utc_departure_time"] = utc_departure_time
        if headsign is not UNSET:
            field_dict["headsign"] = headsign
        if arrival_time is not UNSET:
            field_dict["arrival_time"] = arrival_time
        if journey_pattern_point is not UNSET:
            field_dict["journey_pattern_point"] = journey_pattern_point
        if departure_time is not UNSET:
            field_dict["departure_time"] = departure_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.journey_pattern_point import JourneyPatternPoint
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        utc_arrival_time = d.pop("utc_arrival_time", UNSET)

        utc_departure_time = d.pop("utc_departure_time", UNSET)

        headsign = d.pop("headsign", UNSET)

        arrival_time = d.pop("arrival_time", UNSET)

        _journey_pattern_point = d.pop("journey_pattern_point", UNSET)
        journey_pattern_point: JourneyPatternPoint | Unset
        if isinstance(_journey_pattern_point, Unset):
            journey_pattern_point = UNSET
        else:
            journey_pattern_point = JourneyPatternPoint.from_dict(_journey_pattern_point)

        departure_time = d.pop("departure_time", UNSET)

        stop_time = cls(
            stop_point=stop_point,
            utc_arrival_time=utc_arrival_time,
            utc_departure_time=utc_departure_time,
            headsign=headsign,
            arrival_time=arrival_time,
            journey_pattern_point=journey_pattern_point,
            departure_time=departure_time,
        )

        stop_time.additional_properties = d
        return stop_time

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
