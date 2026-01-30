from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CellLatSchema")


@_attrs_define
class CellLatSchema:
    min_lat: float | Unset = UNSET
    max_lat: float | Unset = UNSET
    center_lat: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_lat = self.min_lat

        max_lat = self.max_lat

        center_lat = self.center_lat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_lat is not UNSET:
            field_dict["min_lat"] = min_lat
        if max_lat is not UNSET:
            field_dict["max_lat"] = max_lat
        if center_lat is not UNSET:
            field_dict["center_lat"] = center_lat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_lat = d.pop("min_lat", UNSET)

        max_lat = d.pop("max_lat", UNSET)

        center_lat = d.pop("center_lat", UNSET)

        cell_lat_schema = cls(
            min_lat=min_lat,
            max_lat=max_lat,
            center_lat=center_lat,
        )

        cell_lat_schema.additional_properties = d
        return cell_lat_schema

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
