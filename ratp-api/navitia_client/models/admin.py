from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coord import Coord


T = TypeVar("T", bound="Admin")


@_attrs_define
class Admin:
    """
    Attributes:
        name (str): Name of the object
        id (str): Identifier of the object
        zip_code (str):
        insee (str | Unset):
        level (int | Unset):
        coord (Coord | Unset):
        label (str | Unset):
    """

    name: str
    id: str
    zip_code: str
    insee: str | Unset = UNSET
    level: int | Unset = UNSET
    coord: Coord | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        zip_code = self.zip_code

        insee = self.insee

        level = self.level

        coord: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coord, Unset):
            coord = self.coord.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "zip_code": zip_code,
            }
        )
        if insee is not UNSET:
            field_dict["insee"] = insee
        if level is not UNSET:
            field_dict["level"] = level
        if coord is not UNSET:
            field_dict["coord"] = coord
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coord import Coord

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id")

        zip_code = d.pop("zip_code")

        insee = d.pop("insee", UNSET)

        level = d.pop("level", UNSET)

        _coord = d.pop("coord", UNSET)
        coord: Coord | Unset
        if isinstance(_coord, Unset):
            coord = UNSET
        else:
            coord = Coord.from_dict(_coord)

        label = d.pop("label", UNSET)

        admin = cls(
            name=name,
            id=id,
            zip_code=zip_code,
            insee=insee,
            level=level,
            coord=coord,
            label=label,
        )

        admin.additional_properties = d
        return admin

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
