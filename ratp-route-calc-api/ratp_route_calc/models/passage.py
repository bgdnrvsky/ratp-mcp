from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema
    from ..models.route import Route
    from ..models.stop_date_time import StopDateTime
    from ..models.stop_point import StopPoint
    from ..models.vj_display_information import VJDisplayInformation


T = TypeVar("T", bound="Passage")


@_attrs_define
class Passage:
    display_informations: VJDisplayInformation | Unset = UNSET
    stop_point: StopPoint | Unset = UNSET
    route: Route | Unset = UNSET
    links: list[LinkSchema] | Unset = UNSET
    stop_date_time: StopDateTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_informations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_informations, Unset):
            display_informations = self.display_informations.to_dict()

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        route: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        stop_date_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_date_time, Unset):
            stop_date_time = self.stop_date_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_informations is not UNSET:
            field_dict["display_informations"] = display_informations
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if route is not UNSET:
            field_dict["route"] = route
        if links is not UNSET:
            field_dict["links"] = links
        if stop_date_time is not UNSET:
            field_dict["stop_date_time"] = stop_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_schema import LinkSchema
        from ..models.route import Route
        from ..models.stop_date_time import StopDateTime
        from ..models.stop_point import StopPoint
        from ..models.vj_display_information import VJDisplayInformation

        d = dict(src_dict)
        _display_informations = d.pop("display_informations", UNSET)
        display_informations: VJDisplayInformation | Unset
        if isinstance(_display_informations, Unset):
            display_informations = UNSET
        else:
            display_informations = VJDisplayInformation.from_dict(_display_informations)

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        _route = d.pop("route", UNSET)
        route: Route | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = Route.from_dict(_route)

        _links = d.pop("links", UNSET)
        links: list[LinkSchema] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = LinkSchema.from_dict(links_item_data)

                links.append(links_item)

        _stop_date_time = d.pop("stop_date_time", UNSET)
        stop_date_time: StopDateTime | Unset
        if isinstance(_stop_date_time, Unset):
            stop_date_time = UNSET
        else:
            stop_date_time = StopDateTime.from_dict(_stop_date_time)

        passage = cls(
            display_informations=display_informations,
            stop_point=stop_point,
            route=route,
            links=links,
            stop_date_time=stop_date_time,
        )

        passage.additional_properties = d
        return passage

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
