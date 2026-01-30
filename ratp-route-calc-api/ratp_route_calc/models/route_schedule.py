from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema
    from ..models.multi_line_string_schema import MultiLineStringSchema
    from ..models.route_display_information import RouteDisplayInformation
    from ..models.table import Table


T = TypeVar("T", bound="RouteSchedule")


@_attrs_define
class RouteSchedule:
    additional_informations: str
    display_informations: RouteDisplayInformation | Unset = UNSET
    table: Table | Unset = UNSET
    geojson: MultiLineStringSchema | Unset = UNSET
    links: list[LinkSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_informations = self.additional_informations

        display_informations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_informations, Unset):
            display_informations = self.display_informations.to_dict()

        table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        geojson: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geojson, Unset):
            geojson = self.geojson.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "additional_informations": additional_informations,
            }
        )
        if display_informations is not UNSET:
            field_dict["display_informations"] = display_informations
        if table is not UNSET:
            field_dict["table"] = table
        if geojson is not UNSET:
            field_dict["geojson"] = geojson
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_schema import LinkSchema
        from ..models.multi_line_string_schema import MultiLineStringSchema
        from ..models.route_display_information import RouteDisplayInformation
        from ..models.table import Table

        d = dict(src_dict)
        additional_informations = d.pop("additional_informations")

        _display_informations = d.pop("display_informations", UNSET)
        display_informations: RouteDisplayInformation | Unset
        if isinstance(_display_informations, Unset):
            display_informations = UNSET
        else:
            display_informations = RouteDisplayInformation.from_dict(_display_informations)

        _table = d.pop("table", UNSET)
        table: Table | Unset
        if isinstance(_table, Unset):
            table = UNSET
        else:
            table = Table.from_dict(_table)

        _geojson = d.pop("geojson", UNSET)
        geojson: MultiLineStringSchema | Unset
        if isinstance(_geojson, Unset):
            geojson = UNSET
        else:
            geojson = MultiLineStringSchema.from_dict(_geojson)

        _links = d.pop("links", UNSET)
        links: list[LinkSchema] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = LinkSchema.from_dict(links_item_data)

                links.append(links_item)

        route_schedule = cls(
            additional_informations=additional_informations,
            display_informations=display_informations,
            table=table,
            geojson=geojson,
            links=links,
        )

        route_schedule.additional_properties = d
        return route_schedule

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
