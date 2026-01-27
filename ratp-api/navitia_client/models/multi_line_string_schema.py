from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiLineStringSchema")


@_attrs_define
class MultiLineStringSchema:
    """
    Attributes:
        type_ (str | Unset):
        coordinates (list[list[list[float]]] | Unset):
    """

    type_: str | Unset = UNSET
    coordinates: list[list[list[float]]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        coordinates: list[list[list[float]]] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item = []
                for coordinates_item_item_data in coordinates_item_data:
                    coordinates_item_item = coordinates_item_item_data

                    coordinates_item.append(coordinates_item_item)

                coordinates.append(coordinates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: list[list[list[float]]] | Unset = UNSET
        if _coordinates is not UNSET:
            coordinates = []
            for coordinates_item_data in _coordinates:
                coordinates_item = []
                _coordinates_item = coordinates_item_data
                for coordinates_item_item_data in _coordinates_item:
                    coordinates_item_item = cast(list[float], coordinates_item_item_data)

                    coordinates_item.append(coordinates_item_item)

                coordinates.append(coordinates_item)

        multi_line_string_schema = cls(
            type_=type_,
            coordinates=coordinates,
        )

        multi_line_string_schema.additional_properties = d
        return multi_line_string_schema

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
