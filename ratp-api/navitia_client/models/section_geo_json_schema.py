from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.section_geo_json_schema_properties_item import SectionGeoJsonSchemaPropertiesItem


T = TypeVar("T", bound="SectionGeoJsonSchema")


@_attrs_define
class SectionGeoJsonSchema:
    """
    Attributes:
        type_ (str | Unset):
        properties (list[SectionGeoJsonSchemaPropertiesItem] | Unset):
        coordinates (list[list[float]] | Unset):
    """

    type_: str | Unset = UNSET
    properties: list[SectionGeoJsonSchemaPropertiesItem] | Unset = UNSET
    coordinates: list[list[float]] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        coordinates: list[list[float]] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item = coordinates_item_data

                coordinates.append(coordinates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.section_geo_json_schema_properties_item import SectionGeoJsonSchemaPropertiesItem

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[SectionGeoJsonSchemaPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = SectionGeoJsonSchemaPropertiesItem.from_dict(properties_item_data)

                properties.append(properties_item)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: list[list[float]] | Unset = UNSET
        if _coordinates is not UNSET:
            coordinates = []
            for coordinates_item_data in _coordinates:
                coordinates_item = cast(list[float], coordinates_item_data)

                coordinates.append(coordinates_item)

        section_geo_json_schema = cls(
            type_=type_,
            properties=properties,
            coordinates=coordinates,
        )

        section_geo_json_schema.additional_properties = d
        return section_geo_json_schema

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
