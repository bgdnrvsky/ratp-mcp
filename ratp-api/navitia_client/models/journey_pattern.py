from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.journey_pattern_point import JourneyPatternPoint
    from ..models.route import Route


T = TypeVar("T", bound="JourneyPattern")


@_attrs_define
class JourneyPattern:
    """
    Attributes:
        name (str): Name of the object
        id (str): Identifier of the object
        route (Route | Unset):
        journey_pattern_points (list[JourneyPatternPoint] | Unset):
    """

    name: str
    id: str
    route: Route | Unset = UNSET
    journey_pattern_points: list[JourneyPatternPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        route: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        journey_pattern_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.journey_pattern_points, Unset):
            journey_pattern_points = []
            for journey_pattern_points_item_data in self.journey_pattern_points:
                journey_pattern_points_item = journey_pattern_points_item_data.to_dict()
                journey_pattern_points.append(journey_pattern_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )
        if route is not UNSET:
            field_dict["route"] = route
        if journey_pattern_points is not UNSET:
            field_dict["journey_pattern_points"] = journey_pattern_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.journey_pattern_point import JourneyPatternPoint
        from ..models.route import Route

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id")

        _route = d.pop("route", UNSET)
        route: Route | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = Route.from_dict(_route)

        _journey_pattern_points = d.pop("journey_pattern_points", UNSET)
        journey_pattern_points: list[JourneyPatternPoint] | Unset = UNSET
        if _journey_pattern_points is not UNSET:
            journey_pattern_points = []
            for journey_pattern_points_item_data in _journey_pattern_points:
                journey_pattern_points_item = JourneyPatternPoint.from_dict(journey_pattern_points_item_data)

                journey_pattern_points.append(journey_pattern_points_item)

        journey_pattern = cls(
            name=name,
            id=id,
            route=route,
            journey_pattern_points=journey_pattern_points,
        )

        journey_pattern.additional_properties = d
        return journey_pattern

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
