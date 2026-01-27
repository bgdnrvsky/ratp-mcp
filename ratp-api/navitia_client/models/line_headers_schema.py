from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cell_lat_schema import CellLatSchema


T = TypeVar("T", bound="LineHeadersSchema")


@_attrs_define
class LineHeadersSchema:
    """
    Attributes:
        cell_lat (CellLatSchema):
    """

    cell_lat: CellLatSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cell_lat = self.cell_lat.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cell_lat": cell_lat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_lat_schema import CellLatSchema

        d = dict(src_dict)
        cell_lat = CellLatSchema.from_dict(d.pop("cell_lat"))

        line_headers_schema = cls(
            cell_lat=cell_lat,
        )

        line_headers_schema.additional_properties = d
        return line_headers_schema

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
