from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.coord import Coord


T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        name (str): Name of the object
        house_number (int):
        id (str): Identifier of the object
        coord (Coord | Unset):
        label (str | Unset):
        administrative_regions (list[Admin] | Unset):
    """

    name: str
    house_number: int
    id: str
    coord: Coord | Unset = UNSET
    label: str | Unset = UNSET
    administrative_regions: list[Admin] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        house_number = self.house_number

        id = self.id

        coord: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coord, Unset):
            coord = self.coord.to_dict()

        label = self.label

        administrative_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.administrative_regions, Unset):
            administrative_regions = []
            for administrative_regions_item_data in self.administrative_regions:
                administrative_regions_item = administrative_regions_item_data.to_dict()
                administrative_regions.append(administrative_regions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "house_number": house_number,
                "id": id,
            }
        )
        if coord is not UNSET:
            field_dict["coord"] = coord
        if label is not UNSET:
            field_dict["label"] = label
        if administrative_regions is not UNSET:
            field_dict["administrative_regions"] = administrative_regions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.coord import Coord

        d = dict(src_dict)
        name = d.pop("name")

        house_number = d.pop("house_number")

        id = d.pop("id")

        _coord = d.pop("coord", UNSET)
        coord: Coord | Unset
        if isinstance(_coord, Unset):
            coord = UNSET
        else:
            coord = Coord.from_dict(_coord)

        label = d.pop("label", UNSET)

        _administrative_regions = d.pop("administrative_regions", UNSET)
        administrative_regions: list[Admin] | Unset = UNSET
        if _administrative_regions is not UNSET:
            administrative_regions = []
            for administrative_regions_item_data in _administrative_regions:
                administrative_regions_item = Admin.from_dict(administrative_regions_item_data)

                administrative_regions.append(administrative_regions_item)

        address = cls(
            name=name,
            house_number=house_number,
            id=id,
            coord=coord,
            label=label,
            administrative_regions=administrative_regions,
        )

        address.additional_properties = d
        return address

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
