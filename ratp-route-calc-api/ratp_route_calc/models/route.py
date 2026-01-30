from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_is_frequence import RouteIsFrequence
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code import Code
    from ..models.comment import Comment
    from ..models.line import Line
    from ..models.link_schema import LinkSchema
    from ..models.multi_line_string_schema import MultiLineStringSchema
    from ..models.physical_mode import PhysicalMode
    from ..models.place import Place
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="Route")


@_attrs_define
class Route:
    name: str
    """ Name of the object """
    links: list[LinkSchema]
    direction_type: str
    id: str
    """ Identifier of the object """
    direction: Place | Unset = UNSET
    codes: list[Code] | Unset = UNSET
    physical_modes: list[PhysicalMode] | Unset = UNSET
    is_frequence: RouteIsFrequence | Unset = UNSET
    comments: list[Comment] | Unset = UNSET
    geojson: MultiLineStringSchema | Unset = UNSET
    stop_points: list[StopPoint] | Unset = UNSET
    line: Line | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        direction_type = self.direction_type

        id = self.id

        direction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()
                codes.append(codes_item)

        physical_modes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.physical_modes, Unset):
            physical_modes = []
            for physical_modes_item_data in self.physical_modes:
                physical_modes_item = physical_modes_item_data.to_dict()
                physical_modes.append(physical_modes_item)

        is_frequence: str | Unset = UNSET
        if not isinstance(self.is_frequence, Unset):
            is_frequence = self.is_frequence.value

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        geojson: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geojson, Unset):
            geojson = self.geojson.to_dict()

        stop_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_points, Unset):
            stop_points = []
            for stop_points_item_data in self.stop_points:
                stop_points_item = stop_points_item_data.to_dict()
                stop_points.append(stop_points_item)

        line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "links": links,
                "direction_type": direction_type,
                "id": id,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if codes is not UNSET:
            field_dict["codes"] = codes
        if physical_modes is not UNSET:
            field_dict["physical_modes"] = physical_modes
        if is_frequence is not UNSET:
            field_dict["is_frequence"] = is_frequence
        if comments is not UNSET:
            field_dict["comments"] = comments
        if geojson is not UNSET:
            field_dict["geojson"] = geojson
        if stop_points is not UNSET:
            field_dict["stop_points"] = stop_points
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code import Code
        from ..models.comment import Comment
        from ..models.line import Line
        from ..models.link_schema import LinkSchema
        from ..models.multi_line_string_schema import MultiLineStringSchema
        from ..models.physical_mode import PhysicalMode
        from ..models.place import Place
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        name = d.pop("name")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        direction_type = d.pop("direction_type")

        id = d.pop("id")

        _direction = d.pop("direction", UNSET)
        direction: Place | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = Place.from_dict(_direction)

        _codes = d.pop("codes", UNSET)
        codes: list[Code] | Unset = UNSET
        if _codes is not UNSET:
            codes = []
            for codes_item_data in _codes:
                codes_item = Code.from_dict(codes_item_data)

                codes.append(codes_item)

        _physical_modes = d.pop("physical_modes", UNSET)
        physical_modes: list[PhysicalMode] | Unset = UNSET
        if _physical_modes is not UNSET:
            physical_modes = []
            for physical_modes_item_data in _physical_modes:
                physical_modes_item = PhysicalMode.from_dict(physical_modes_item_data)

                physical_modes.append(physical_modes_item)

        _is_frequence = d.pop("is_frequence", UNSET)
        is_frequence: RouteIsFrequence | Unset
        if isinstance(_is_frequence, Unset):
            is_frequence = UNSET
        else:
            is_frequence = RouteIsFrequence(_is_frequence)

        _comments = d.pop("comments", UNSET)
        comments: list[Comment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = Comment.from_dict(comments_item_data)

                comments.append(comments_item)

        _geojson = d.pop("geojson", UNSET)
        geojson: MultiLineStringSchema | Unset
        if isinstance(_geojson, Unset):
            geojson = UNSET
        else:
            geojson = MultiLineStringSchema.from_dict(_geojson)

        _stop_points = d.pop("stop_points", UNSET)
        stop_points: list[StopPoint] | Unset = UNSET
        if _stop_points is not UNSET:
            stop_points = []
            for stop_points_item_data in _stop_points:
                stop_points_item = StopPoint.from_dict(stop_points_item_data)

                stop_points.append(stop_points_item)

        _line = d.pop("line", UNSET)
        line: Line | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Line.from_dict(_line)

        route = cls(
            name=name,
            links=links,
            direction_type=direction_type,
            id=id,
            direction=direction,
            codes=codes,
            physical_modes=physical_modes,
            is_frequence=is_frequence,
            comments=comments,
            geojson=geojson,
            stop_points=stop_points,
            line=line,
        )

        route.additional_properties = d
        return route

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
