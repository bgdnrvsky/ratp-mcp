from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.impacted_stop_stop_time_effect import ImpactedStopStopTimeEffect
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="ImpactedStop")


@_attrs_define
class ImpactedStop:
    is_detour: bool
    cause: str
    amended_arrival_time: str | Unset = UNSET
    stop_point: StopPoint | Unset = UNSET
    stop_time_effect: ImpactedStopStopTimeEffect | Unset = UNSET
    departure_status: str | Unset = UNSET
    amended_departure_time: str | Unset = UNSET
    base_arrival_time: str | Unset = UNSET
    base_departure_time: str | Unset = UNSET
    arrival_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_detour = self.is_detour

        cause = self.cause

        amended_arrival_time = self.amended_arrival_time

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        stop_time_effect: str | Unset = UNSET
        if not isinstance(self.stop_time_effect, Unset):
            stop_time_effect = self.stop_time_effect.value

        departure_status = self.departure_status

        amended_departure_time = self.amended_departure_time

        base_arrival_time = self.base_arrival_time

        base_departure_time = self.base_departure_time

        arrival_status = self.arrival_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_detour": is_detour,
                "cause": cause,
            }
        )
        if amended_arrival_time is not UNSET:
            field_dict["amended_arrival_time"] = amended_arrival_time
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if stop_time_effect is not UNSET:
            field_dict["stop_time_effect"] = stop_time_effect
        if departure_status is not UNSET:
            field_dict["departure_status"] = departure_status
        if amended_departure_time is not UNSET:
            field_dict["amended_departure_time"] = amended_departure_time
        if base_arrival_time is not UNSET:
            field_dict["base_arrival_time"] = base_arrival_time
        if base_departure_time is not UNSET:
            field_dict["base_departure_time"] = base_departure_time
        if arrival_status is not UNSET:
            field_dict["arrival_status"] = arrival_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        is_detour = d.pop("is_detour")

        cause = d.pop("cause")

        amended_arrival_time = d.pop("amended_arrival_time", UNSET)

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        _stop_time_effect = d.pop("stop_time_effect", UNSET)
        stop_time_effect: ImpactedStopStopTimeEffect | Unset
        if isinstance(_stop_time_effect, Unset):
            stop_time_effect = UNSET
        else:
            stop_time_effect = ImpactedStopStopTimeEffect(_stop_time_effect)

        departure_status = d.pop("departure_status", UNSET)

        amended_departure_time = d.pop("amended_departure_time", UNSET)

        base_arrival_time = d.pop("base_arrival_time", UNSET)

        base_departure_time = d.pop("base_departure_time", UNSET)

        arrival_status = d.pop("arrival_status", UNSET)

        impacted_stop = cls(
            is_detour=is_detour,
            cause=cause,
            amended_arrival_time=amended_arrival_time,
            stop_point=stop_point,
            stop_time_effect=stop_time_effect,
            departure_status=departure_status,
            amended_departure_time=amended_departure_time,
            base_arrival_time=base_arrival_time,
            base_departure_time=base_departure_time,
            arrival_status=arrival_status,
        )

        impacted_stop.additional_properties = d
        return impacted_stop

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
