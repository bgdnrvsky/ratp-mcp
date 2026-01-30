from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stands_status import StandsStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Stands")


@_attrs_define
class Stands:
    status: StandsStatus | Unset = UNSET
    available_places: int | Unset = UNSET
    available_bikes: int | Unset = UNSET
    total_stands: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        available_places = self.available_places

        available_bikes = self.available_bikes

        total_stands = self.total_stands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if available_places is not UNSET:
            field_dict["available_places"] = available_places
        if available_bikes is not UNSET:
            field_dict["available_bikes"] = available_bikes
        if total_stands is not UNSET:
            field_dict["total_stands"] = total_stands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: StandsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StandsStatus(_status)

        available_places = d.pop("available_places", UNSET)

        available_bikes = d.pop("available_bikes", UNSET)

        total_stands = d.pop("total_stands", UNSET)

        stands = cls(
            status=status,
            available_places=available_places,
            available_bikes=available_bikes,
            total_stands=total_stands,
        )

        stands.additional_properties = d
        return stands

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
