from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.line_headers_schema import LineHeadersSchema
    from ..models.lines_schema import LinesSchema


T = TypeVar("T", bound="HeatMatrixSchema")


@_attrs_define
class HeatMatrixSchema:
    """
    Attributes:
        line_headers (list[LineHeadersSchema]):
        lines (list[LinesSchema]):
    """

    line_headers: list[LineHeadersSchema]
    lines: list[LinesSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_headers = []
        for line_headers_item_data in self.line_headers:
            line_headers_item = line_headers_item_data.to_dict()
            line_headers.append(line_headers_item)

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_headers": line_headers,
                "lines": lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_headers_schema import LineHeadersSchema
        from ..models.lines_schema import LinesSchema

        d = dict(src_dict)
        line_headers = []
        _line_headers = d.pop("line_headers")
        for line_headers_item_data in _line_headers:
            line_headers_item = LineHeadersSchema.from_dict(line_headers_item_data)

            line_headers.append(line_headers_item)

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = LinesSchema.from_dict(lines_item_data)

            lines.append(lines_item)

        heat_matrix_schema = cls(
            line_headers=line_headers,
            lines=lines,
        )

        heat_matrix_schema.additional_properties = d
        return heat_matrix_schema

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
