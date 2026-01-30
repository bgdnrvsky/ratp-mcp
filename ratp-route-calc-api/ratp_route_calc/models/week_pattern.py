from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WeekPattern")


@_attrs_define
class WeekPattern:
    monday: bool | Unset = UNSET
    tuesday: bool | Unset = UNSET
    friday: bool | Unset = UNSET
    wednesday: bool | Unset = UNSET
    thursday: bool | Unset = UNSET
    sunday: bool | Unset = UNSET
    saturday: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday = self.monday

        tuesday = self.tuesday

        friday = self.friday

        wednesday = self.wednesday

        thursday = self.thursday

        sunday = self.sunday

        saturday = self.saturday

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        friday = d.pop("friday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        sunday = d.pop("sunday", UNSET)

        saturday = d.pop("saturday", UNSET)

        week_pattern = cls(
            monday=monday,
            tuesday=tuesday,
            friday=friday,
            wednesday=wednesday,
            thursday=thursday,
            sunday=sunday,
            saturday=saturday,
        )

        week_pattern.additional_properties = d
        return week_pattern

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
