from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CarPark")


@_attrs_define
class CarPark:
    """
    Attributes:
        available (int | Unset):
        total_places (int | Unset):
        occupied_prm (int | Unset):
        occupied (int | Unset):
        available_prm (int | Unset):
    """

    available: int | Unset = UNSET
    total_places: int | Unset = UNSET
    occupied_prm: int | Unset = UNSET
    occupied: int | Unset = UNSET
    available_prm: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        total_places = self.total_places

        occupied_prm = self.occupied_prm

        occupied = self.occupied

        available_prm = self.available_prm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if total_places is not UNSET:
            field_dict["total_places"] = total_places
        if occupied_prm is not UNSET:
            field_dict["occupied_PRM"] = occupied_prm
        if occupied is not UNSET:
            field_dict["occupied"] = occupied
        if available_prm is not UNSET:
            field_dict["available_PRM"] = available_prm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available", UNSET)

        total_places = d.pop("total_places", UNSET)

        occupied_prm = d.pop("occupied_PRM", UNSET)

        occupied = d.pop("occupied", UNSET)

        available_prm = d.pop("available_PRM", UNSET)

        car_park = cls(
            available=available,
            total_places=total_places,
            occupied_prm=occupied_prm,
            occupied=occupied,
            available_prm=available_prm,
        )

        car_park.additional_properties = d
        return car_park

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
