from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndividualRating")


@_attrs_define
class IndividualRating:
    """
    Attributes:
        value (float):
        count (int | Unset):
        scale_min (float | Unset):
        scale_max (float | Unset):
    """

    value: float
    count: int | Unset = UNSET
    scale_min: float | Unset = UNSET
    scale_max: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        count = self.count

        scale_min = self.scale_min

        scale_max = self.scale_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if scale_min is not UNSET:
            field_dict["scale_min"] = scale_min
        if scale_max is not UNSET:
            field_dict["scale_max"] = scale_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        count = d.pop("count", UNSET)

        scale_min = d.pop("scale_min", UNSET)

        scale_max = d.pop("scale_max", UNSET)

        individual_rating = cls(
            value=value,
            count=count,
            scale_min=scale_min,
            scale_max=scale_max,
        )

        individual_rating.additional_properties = d
        return individual_rating

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
