from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.equipment_details_embedded_type import EquipmentDetailsEmbeddedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_availability import CurrentAvailability


T = TypeVar("T", bound="EquipmentDetails")


@_attrs_define
class EquipmentDetails:
    """
    Attributes:
        embedded_type (EquipmentDetailsEmbeddedType | Unset):
        id (str | Unset):
        name (str | Unset):
        current_availability (CurrentAvailability | Unset):
    """

    embedded_type: EquipmentDetailsEmbeddedType | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    current_availability: CurrentAvailability | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedded_type: str | Unset = UNSET
        if not isinstance(self.embedded_type, Unset):
            embedded_type = self.embedded_type.value

        id = self.id

        name = self.name

        current_availability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_availability, Unset):
            current_availability = self.current_availability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embedded_type is not UNSET:
            field_dict["embedded_type"] = embedded_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if current_availability is not UNSET:
            field_dict["current_availability"] = current_availability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.current_availability import CurrentAvailability

        d = dict(src_dict)
        _embedded_type = d.pop("embedded_type", UNSET)
        embedded_type: EquipmentDetailsEmbeddedType | Unset
        if isinstance(_embedded_type, Unset):
            embedded_type = UNSET
        else:
            embedded_type = EquipmentDetailsEmbeddedType(_embedded_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _current_availability = d.pop("current_availability", UNSET)
        current_availability: CurrentAvailability | Unset
        if isinstance(_current_availability, Unset):
            current_availability = UNSET
        else:
            current_availability = CurrentAvailability.from_dict(_current_availability)

        equipment_details = cls(
            embedded_type=embedded_type,
            id=id,
            name=name,
            current_availability=current_availability,
        )

        equipment_details.additional_properties = d
        return equipment_details

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
