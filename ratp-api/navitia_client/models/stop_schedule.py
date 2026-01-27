from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_time_type import DateTimeType
    from ..models.link_schema import LinkSchema
    from ..models.route import Route
    from ..models.route_display_information import RouteDisplayInformation
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="StopSchedule")


@_attrs_define
class StopSchedule:
    """
    Attributes:
        date_times (list[DateTimeType]):
        additional_informations (str):
        stop_point (StopPoint | Unset):
        links (list[LinkSchema] | Unset):
        route (Route | Unset):
        display_informations (RouteDisplayInformation | Unset):
        last_datetime (DateTimeType | Unset):
        first_datetime (DateTimeType | Unset):
    """

    date_times: list[DateTimeType]
    additional_informations: str
    stop_point: StopPoint | Unset = UNSET
    links: list[LinkSchema] | Unset = UNSET
    route: Route | Unset = UNSET
    display_informations: RouteDisplayInformation | Unset = UNSET
    last_datetime: DateTimeType | Unset = UNSET
    first_datetime: DateTimeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_times = []
        for date_times_item_data in self.date_times:
            date_times_item = date_times_item_data.to_dict()
            date_times.append(date_times_item)

        additional_informations = self.additional_informations

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        route: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        display_informations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_informations, Unset):
            display_informations = self.display_informations.to_dict()

        last_datetime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_datetime, Unset):
            last_datetime = self.last_datetime.to_dict()

        first_datetime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_datetime, Unset):
            first_datetime = self.first_datetime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_times": date_times,
                "additional_informations": additional_informations,
            }
        )
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if links is not UNSET:
            field_dict["links"] = links
        if route is not UNSET:
            field_dict["route"] = route
        if display_informations is not UNSET:
            field_dict["display_informations"] = display_informations
        if last_datetime is not UNSET:
            field_dict["last_datetime"] = last_datetime
        if first_datetime is not UNSET:
            field_dict["first_datetime"] = first_datetime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_time_type import DateTimeType
        from ..models.link_schema import LinkSchema
        from ..models.route import Route
        from ..models.route_display_information import RouteDisplayInformation
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        date_times = []
        _date_times = d.pop("date_times")
        for date_times_item_data in _date_times:
            date_times_item = DateTimeType.from_dict(date_times_item_data)

            date_times.append(date_times_item)

        additional_informations = d.pop("additional_informations")

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        _links = d.pop("links", UNSET)
        links: list[LinkSchema] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = LinkSchema.from_dict(links_item_data)

                links.append(links_item)

        _route = d.pop("route", UNSET)
        route: Route | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = Route.from_dict(_route)

        _display_informations = d.pop("display_informations", UNSET)
        display_informations: RouteDisplayInformation | Unset
        if isinstance(_display_informations, Unset):
            display_informations = UNSET
        else:
            display_informations = RouteDisplayInformation.from_dict(_display_informations)

        _last_datetime = d.pop("last_datetime", UNSET)
        last_datetime: DateTimeType | Unset
        if isinstance(_last_datetime, Unset):
            last_datetime = UNSET
        else:
            last_datetime = DateTimeType.from_dict(_last_datetime)

        _first_datetime = d.pop("first_datetime", UNSET)
        first_datetime: DateTimeType | Unset
        if isinstance(_first_datetime, Unset):
            first_datetime = UNSET
        else:
            first_datetime = DateTimeType.from_dict(_first_datetime)

        stop_schedule = cls(
            date_times=date_times,
            additional_informations=additional_informations,
            stop_point=stop_point,
            links=links,
            route=route,
            display_informations=display_informations,
            last_datetime=last_datetime,
            first_datetime=first_datetime,
        )

        stop_schedule.additional_properties = d
        return stop_schedule

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
