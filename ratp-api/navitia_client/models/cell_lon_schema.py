from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CellLonSchema")


@_attrs_define
class CellLonSchema:
    """
    Attributes:
        min_lon (float | Unset):
        center_lon (float | Unset):
        max_lon (float | Unset):
    """

    min_lon: float | Unset = UNSET
    center_lon: float | Unset = UNSET
    max_lon: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_lon = self.min_lon

        center_lon = self.center_lon

        max_lon = self.max_lon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_lon is not UNSET:
            field_dict["min_lon"] = min_lon
        if center_lon is not UNSET:
            field_dict["center_lon"] = center_lon
        if max_lon is not UNSET:
            field_dict["max_lon"] = max_lon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_lon = d.pop("min_lon", UNSET)

        center_lon = d.pop("center_lon", UNSET)

        max_lon = d.pop("max_lon", UNSET)

        cell_lon_schema = cls(
            min_lon=min_lon,
            center_lon=center_lon,
            max_lon=max_lon,
        )

        cell_lon_schema.additional_properties = d
        return cell_lon_schema

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
