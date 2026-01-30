from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoStatus")


@_attrs_define
class GeoStatus:
    street_network_sources: list[str]
    poi_sources: list[str]
    nb_admins_from_cities: int | Unset = UNSET
    nb_addresses: int | Unset = UNSET
    nb_admins: int | Unset = UNSET
    nb_pois: int | Unset = UNSET
    nb_ways: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street_network_sources = self.street_network_sources

        poi_sources = self.poi_sources

        nb_admins_from_cities = self.nb_admins_from_cities

        nb_addresses = self.nb_addresses

        nb_admins = self.nb_admins

        nb_pois = self.nb_pois

        nb_ways = self.nb_ways

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "street_network_sources": street_network_sources,
                "poi_sources": poi_sources,
            }
        )
        if nb_admins_from_cities is not UNSET:
            field_dict["nb_admins_from_cities"] = nb_admins_from_cities
        if nb_addresses is not UNSET:
            field_dict["nb_addresses"] = nb_addresses
        if nb_admins is not UNSET:
            field_dict["nb_admins"] = nb_admins
        if nb_pois is not UNSET:
            field_dict["nb_pois"] = nb_pois
        if nb_ways is not UNSET:
            field_dict["nb_ways"] = nb_ways

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street_network_sources = cast(list[str], d.pop("street_network_sources"))

        poi_sources = cast(list[str], d.pop("poi_sources"))

        nb_admins_from_cities = d.pop("nb_admins_from_cities", UNSET)

        nb_addresses = d.pop("nb_addresses", UNSET)

        nb_admins = d.pop("nb_admins", UNSET)

        nb_pois = d.pop("nb_pois", UNSET)

        nb_ways = d.pop("nb_ways", UNSET)

        geo_status = cls(
            street_network_sources=street_network_sources,
            poi_sources=poi_sources,
            nb_admins_from_cities=nb_admins_from_cities,
            nb_addresses=nb_addresses,
            nb_admins=nb_admins,
            nb_pois=nb_pois,
            nb_ways=nb_ways,
        )

        geo_status.additional_properties = d
        return geo_status

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
