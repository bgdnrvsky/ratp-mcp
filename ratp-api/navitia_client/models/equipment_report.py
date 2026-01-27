from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line import Line
    from ..models.stop_area_equipments import StopAreaEquipments


T = TypeVar("T", bound="EquipmentReport")


@_attrs_define
class EquipmentReport:
    """
    Attributes:
        line (Line | Unset):
        stop_area_equipments (list[StopAreaEquipments] | Unset):
    """

    line: Line | Unset = UNSET
    stop_area_equipments: list[StopAreaEquipments] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        stop_area_equipments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_area_equipments, Unset):
            stop_area_equipments = []
            for stop_area_equipments_item_data in self.stop_area_equipments:
                stop_area_equipments_item = stop_area_equipments_item_data.to_dict()
                stop_area_equipments.append(stop_area_equipments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line is not UNSET:
            field_dict["line"] = line
        if stop_area_equipments is not UNSET:
            field_dict["stop_area_equipments"] = stop_area_equipments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line import Line
        from ..models.stop_area_equipments import StopAreaEquipments

        d = dict(src_dict)
        _line = d.pop("line", UNSET)
        line: Line | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Line.from_dict(_line)

        _stop_area_equipments = d.pop("stop_area_equipments", UNSET)
        stop_area_equipments: list[StopAreaEquipments] | Unset = UNSET
        if _stop_area_equipments is not UNSET:
            stop_area_equipments = []
            for stop_area_equipments_item_data in _stop_area_equipments:
                stop_area_equipments_item = StopAreaEquipments.from_dict(stop_area_equipments_item_data)

                stop_area_equipments.append(stop_area_equipments_item)

        equipment_report = cls(
            line=line,
            stop_area_equipments=stop_area_equipments,
        )

        equipment_report.additional_properties = d
        return equipment_report

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
