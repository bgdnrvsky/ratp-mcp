from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Durations")


@_attrs_define
class Durations:
    taxi: int
    """ Total duration by taxi of the journey (seconds) """
    walking: int
    """ Total walking duration of the journey (seconds) """
    car: int
    """ Total duration by car of the journey (seconds) """
    ridesharing: int
    """ Total duration by ridesharing of the journey (seconds) """
    bike: int
    """ Total duration by bike of the journey (seconds) """
    total: int
    """ Total duration of the journey (seconds) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxi = self.taxi

        walking = self.walking

        car = self.car

        ridesharing = self.ridesharing

        bike = self.bike

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxi": taxi,
                "walking": walking,
                "car": car,
                "ridesharing": ridesharing,
                "bike": bike,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        taxi = d.pop("taxi")

        walking = d.pop("walking")

        car = d.pop("car")

        ridesharing = d.pop("ridesharing")

        bike = d.pop("bike")

        total = d.pop("total")

        durations = cls(
            taxi=taxi,
            walking=walking,
            car=car,
            ridesharing=ridesharing,
            bike=bike,
            total=total,
        )

        durations.additional_properties = d
        return durations

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
