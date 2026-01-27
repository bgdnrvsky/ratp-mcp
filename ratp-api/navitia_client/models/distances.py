from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Distances")


@_attrs_define
class Distances:
    """
    Attributes:
        taxi (int): Total distance by taxi of the journey (meters)
        car (int): Total distance by car of the journey (meters)
        walking (int): Total walking distance of the journey (meters)
        bike (int): Total distance by bike of the journey (meters)
        ridesharing (int): Total distance by ridesharing of the journey (meters)
    """

    taxi: int
    car: int
    walking: int
    bike: int
    ridesharing: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxi = self.taxi

        car = self.car

        walking = self.walking

        bike = self.bike

        ridesharing = self.ridesharing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "taxi": taxi,
                "car": car,
                "walking": walking,
                "bike": bike,
                "ridesharing": ridesharing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        taxi = d.pop("taxi")

        car = d.pop("car")

        walking = d.pop("walking")

        bike = d.pop("bike")

        ridesharing = d.pop("ridesharing")

        distances = cls(
            taxi=taxi,
            car=car,
            walking=walking,
            bike=bike,
            ridesharing=ridesharing,
        )

        distances.additional_properties = d
        return distances

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
