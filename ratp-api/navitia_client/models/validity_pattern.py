from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidityPattern")


@_attrs_define
class ValidityPattern:
    """
    Attributes:
        beginning_date (str | Unset):
        days (str | Unset):
    """

    beginning_date: str | Unset = UNSET
    days: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beginning_date = self.beginning_date

        days = self.days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beginning_date is not UNSET:
            field_dict["beginning_date"] = beginning_date
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        beginning_date = d.pop("beginning_date", UNSET)

        days = d.pop("days", UNSET)

        validity_pattern = cls(
            beginning_date=beginning_date,
            days=days,
        )

        validity_pattern.additional_properties = d
        return validity_pattern

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
