from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin import Admin
    from ..models.code import Code
    from ..models.comment import Comment
    from ..models.commercial_mode import CommercialMode
    from ..models.coord import Coord
    from ..models.link_schema import LinkSchema
    from ..models.physical_mode import PhysicalMode
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="StopArea")


@_attrs_define
class StopArea:
    """
    Attributes:
        name (str): Name of the object
        links (list[LinkSchema]):
        id (str): Identifier of the object
        comment (str | Unset):
        codes (list[Code] | Unset):
        physical_modes (list[PhysicalMode] | Unset):
        comments (list[Comment] | Unset):
        label (str | Unset):
            Label of the stop area. The name is directly taken from the data whereas the label is
             something we compute for better traveler information. If you don't know what to display, display the label.
        commercial_modes (list[CommercialMode] | Unset):
        coord (Coord | Unset):
        administrative_regions (list[Admin] | Unset):
        timezone (str | Unset):
        stop_points (list[StopPoint] | Unset):
    """

    name: str
    links: list[LinkSchema]
    id: str
    comment: str | Unset = UNSET
    codes: list[Code] | Unset = UNSET
    physical_modes: list[PhysicalMode] | Unset = UNSET
    comments: list[Comment] | Unset = UNSET
    label: str | Unset = UNSET
    commercial_modes: list[CommercialMode] | Unset = UNSET
    coord: Coord | Unset = UNSET
    administrative_regions: list[Admin] | Unset = UNSET
    timezone: str | Unset = UNSET
    stop_points: list[StopPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        id = self.id

        comment = self.comment

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

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        label = self.label

        commercial_modes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commercial_modes, Unset):
            commercial_modes = []
            for commercial_modes_item_data in self.commercial_modes:
                commercial_modes_item = commercial_modes_item_data.to_dict()
                commercial_modes.append(commercial_modes_item)

        coord: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coord, Unset):
            coord = self.coord.to_dict()

        administrative_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.administrative_regions, Unset):
            administrative_regions = []
            for administrative_regions_item_data in self.administrative_regions:
                administrative_regions_item = administrative_regions_item_data.to_dict()
                administrative_regions.append(administrative_regions_item)

        timezone = self.timezone

        stop_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_points, Unset):
            stop_points = []
            for stop_points_item_data in self.stop_points:
                stop_points_item = stop_points_item_data.to_dict()
                stop_points.append(stop_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "links": links,
                "id": id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if codes is not UNSET:
            field_dict["codes"] = codes
        if physical_modes is not UNSET:
            field_dict["physical_modes"] = physical_modes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if label is not UNSET:
            field_dict["label"] = label
        if commercial_modes is not UNSET:
            field_dict["commercial_modes"] = commercial_modes
        if coord is not UNSET:
            field_dict["coord"] = coord
        if administrative_regions is not UNSET:
            field_dict["administrative_regions"] = administrative_regions
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if stop_points is not UNSET:
            field_dict["stop_points"] = stop_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin import Admin
        from ..models.code import Code
        from ..models.comment import Comment
        from ..models.commercial_mode import CommercialMode
        from ..models.coord import Coord
        from ..models.link_schema import LinkSchema
        from ..models.physical_mode import PhysicalMode
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        name = d.pop("name")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id")

        comment = d.pop("comment", UNSET)

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

        _comments = d.pop("comments", UNSET)
        comments: list[Comment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = Comment.from_dict(comments_item_data)

                comments.append(comments_item)

        label = d.pop("label", UNSET)

        _commercial_modes = d.pop("commercial_modes", UNSET)
        commercial_modes: list[CommercialMode] | Unset = UNSET
        if _commercial_modes is not UNSET:
            commercial_modes = []
            for commercial_modes_item_data in _commercial_modes:
                commercial_modes_item = CommercialMode.from_dict(commercial_modes_item_data)

                commercial_modes.append(commercial_modes_item)

        _coord = d.pop("coord", UNSET)
        coord: Coord | Unset
        if isinstance(_coord, Unset):
            coord = UNSET
        else:
            coord = Coord.from_dict(_coord)

        _administrative_regions = d.pop("administrative_regions", UNSET)
        administrative_regions: list[Admin] | Unset = UNSET
        if _administrative_regions is not UNSET:
            administrative_regions = []
            for administrative_regions_item_data in _administrative_regions:
                administrative_regions_item = Admin.from_dict(administrative_regions_item_data)

                administrative_regions.append(administrative_regions_item)

        timezone = d.pop("timezone", UNSET)

        _stop_points = d.pop("stop_points", UNSET)
        stop_points: list[StopPoint] | Unset = UNSET
        if _stop_points is not UNSET:
            stop_points = []
            for stop_points_item_data in _stop_points:
                stop_points_item = StopPoint.from_dict(stop_points_item_data)

                stop_points.append(stop_points_item)

        stop_area = cls(
            name=name,
            links=links,
            id=id,
            comment=comment,
            codes=codes,
            physical_modes=physical_modes,
            comments=comments,
            label=label,
            commercial_modes=commercial_modes,
            coord=coord,
            administrative_regions=administrative_regions,
            timezone=timezone,
            stop_points=stop_points,
        )

        stop_area.additional_properties = d
        return stop_area

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
