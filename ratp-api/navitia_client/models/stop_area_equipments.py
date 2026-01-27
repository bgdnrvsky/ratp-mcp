from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equipment_details import EquipmentDetails
    from ..models.stop_area import StopArea


T = TypeVar("T", bound="StopAreaEquipments")


@_attrs_define
class StopAreaEquipments:
    """
    Attributes:
        stop_area (StopArea | Unset):
        equipment_details (list[EquipmentDetails] | Unset):
    """

    stop_area: StopArea | Unset = UNSET
    equipment_details: list[EquipmentDetails] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_area, Unset):
            stop_area = self.stop_area.to_dict()

        equipment_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.equipment_details, Unset):
            equipment_details = []
            for equipment_details_item_data in self.equipment_details:
                equipment_details_item = equipment_details_item_data.to_dict()
                equipment_details.append(equipment_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop_area is not UNSET:
            field_dict["stop_area"] = stop_area
        if equipment_details is not UNSET:
            field_dict["equipment_details"] = equipment_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.equipment_details import EquipmentDetails
        from ..models.stop_area import StopArea

        d = dict(src_dict)
        _stop_area = d.pop("stop_area", UNSET)
        stop_area: StopArea | Unset
        if isinstance(_stop_area, Unset):
            stop_area = UNSET
        else:
            stop_area = StopArea.from_dict(_stop_area)

        _equipment_details = d.pop("equipment_details", UNSET)
        equipment_details: list[EquipmentDetails] | Unset = UNSET
        if _equipment_details is not UNSET:
            equipment_details = []
            for equipment_details_item_data in _equipment_details:
                equipment_details_item = EquipmentDetails.from_dict(equipment_details_item_data)

                equipment_details.append(equipment_details_item)

        stop_area_equipments = cls(
            stop_area=stop_area,
            equipment_details=equipment_details,
        )

        stop_area_equipments.additional_properties = d
        return stop_area_equipments

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
