from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cell_lon_schema import CellLonSchema


T = TypeVar("T", bound="LinesSchema")


@_attrs_define
class LinesSchema:
    cell_lon: CellLonSchema
    duration: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell_lon = self.cell_lon.to_dict()

        duration: list[int] | Unset = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cell_lon": cell_lon,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_lon_schema import CellLonSchema

        d = dict(src_dict)
        cell_lon = CellLonSchema.from_dict(d.pop("cell_lon"))

        duration = cast(list[int], d.pop("duration", UNSET))

        lines_schema = cls(
            cell_lon=cell_lon,
            duration=duration,
        )

        lines_schema.additional_properties = d
        return lines_schema

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
