from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line import Line
    from ..models.pt_object import PtObject


T = TypeVar("T", bound="LineReport")


@_attrs_define
class LineReport:
    pt_objects: list[PtObject]
    line: Line | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pt_objects = []
        for pt_objects_item_data in self.pt_objects:
            pt_objects_item = pt_objects_item_data.to_dict()
            pt_objects.append(pt_objects_item)

        line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pt_objects": pt_objects,
            }
        )
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line import Line
        from ..models.pt_object import PtObject

        d = dict(src_dict)
        pt_objects = []
        _pt_objects = d.pop("pt_objects")
        for pt_objects_item_data in _pt_objects:
            pt_objects_item = PtObject.from_dict(pt_objects_item_data)

            pt_objects.append(pt_objects_item)

        _line = d.pop("line", UNSET)
        line: Line | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Line.from_dict(_line)

        line_report = cls(
            pt_objects=pt_objects,
            line=line,
        )

        line_report.additional_properties = d
        return line_report

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
