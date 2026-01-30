from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code import Code
    from ..models.comment import Comment
    from ..models.commercial_mode import CommercialMode
    from ..models.line_group import LineGroup
    from ..models.link_schema import LinkSchema
    from ..models.multi_line_string_schema import MultiLineStringSchema
    from ..models.network import Network
    from ..models.physical_mode import PhysicalMode
    from ..models.property_ import Property
    from ..models.route import Route


T = TypeVar("T", bound="Line")


@_attrs_define
class Line:
    code: str
    links: list[LinkSchema]
    id: str
    """ Identifier of the object """
    name: str
    """ Name of the object """
    comment: str | Unset = UNSET
    properties: list[Property] | Unset = UNSET
    network: Network | Unset = UNSET
    color: str | Unset = UNSET
    routes: list[Route] | Unset = UNSET
    geojson: MultiLineStringSchema | Unset = UNSET
    text_color: str | Unset = UNSET
    physical_modes: list[PhysicalMode] | Unset = UNSET
    codes: list[Code] | Unset = UNSET
    comments: list[Comment] | Unset = UNSET
    closing_time: str | Unset = UNSET
    opening_time: str | Unset = UNSET
    commercial_mode: CommercialMode | Unset = UNSET
    line_groups: list[LineGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        id = self.id

        name = self.name

        comment = self.comment

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        color = self.color

        routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        geojson: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geojson, Unset):
            geojson = self.geojson.to_dict()

        text_color = self.text_color

        physical_modes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.physical_modes, Unset):
            physical_modes = []
            for physical_modes_item_data in self.physical_modes:
                physical_modes_item = physical_modes_item_data.to_dict()
                physical_modes.append(physical_modes_item)

        codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()
                codes.append(codes_item)

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        closing_time = self.closing_time

        opening_time = self.opening_time

        commercial_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commercial_mode, Unset):
            commercial_mode = self.commercial_mode.to_dict()

        line_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_groups, Unset):
            line_groups = []
            for line_groups_item_data in self.line_groups:
                line_groups_item = line_groups_item_data.to_dict()
                line_groups.append(line_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "links": links,
                "id": id,
                "name": name,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if properties is not UNSET:
            field_dict["properties"] = properties
        if network is not UNSET:
            field_dict["network"] = network
        if color is not UNSET:
            field_dict["color"] = color
        if routes is not UNSET:
            field_dict["routes"] = routes
        if geojson is not UNSET:
            field_dict["geojson"] = geojson
        if text_color is not UNSET:
            field_dict["text_color"] = text_color
        if physical_modes is not UNSET:
            field_dict["physical_modes"] = physical_modes
        if codes is not UNSET:
            field_dict["codes"] = codes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if closing_time is not UNSET:
            field_dict["closing_time"] = closing_time
        if opening_time is not UNSET:
            field_dict["opening_time"] = opening_time
        if commercial_mode is not UNSET:
            field_dict["commercial_mode"] = commercial_mode
        if line_groups is not UNSET:
            field_dict["line_groups"] = line_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code import Code
        from ..models.comment import Comment
        from ..models.commercial_mode import CommercialMode
        from ..models.line_group import LineGroup
        from ..models.link_schema import LinkSchema
        from ..models.multi_line_string_schema import MultiLineStringSchema
        from ..models.network import Network
        from ..models.physical_mode import PhysicalMode
        from ..models.property_ import Property
        from ..models.route import Route

        d = dict(src_dict)
        code = d.pop("code")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        id = d.pop("id")

        name = d.pop("name")

        comment = d.pop("comment", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[Property] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = Property.from_dict(properties_item_data)

                properties.append(properties_item)

        _network = d.pop("network", UNSET)
        network: Network | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = Network.from_dict(_network)

        color = d.pop("color", UNSET)

        _routes = d.pop("routes", UNSET)
        routes: list[Route] | Unset = UNSET
        if _routes is not UNSET:
            routes = []
            for routes_item_data in _routes:
                routes_item = Route.from_dict(routes_item_data)

                routes.append(routes_item)

        _geojson = d.pop("geojson", UNSET)
        geojson: MultiLineStringSchema | Unset
        if isinstance(_geojson, Unset):
            geojson = UNSET
        else:
            geojson = MultiLineStringSchema.from_dict(_geojson)

        text_color = d.pop("text_color", UNSET)

        _physical_modes = d.pop("physical_modes", UNSET)
        physical_modes: list[PhysicalMode] | Unset = UNSET
        if _physical_modes is not UNSET:
            physical_modes = []
            for physical_modes_item_data in _physical_modes:
                physical_modes_item = PhysicalMode.from_dict(physical_modes_item_data)

                physical_modes.append(physical_modes_item)

        _codes = d.pop("codes", UNSET)
        codes: list[Code] | Unset = UNSET
        if _codes is not UNSET:
            codes = []
            for codes_item_data in _codes:
                codes_item = Code.from_dict(codes_item_data)

                codes.append(codes_item)

        _comments = d.pop("comments", UNSET)
        comments: list[Comment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = Comment.from_dict(comments_item_data)

                comments.append(comments_item)

        closing_time = d.pop("closing_time", UNSET)

        opening_time = d.pop("opening_time", UNSET)

        _commercial_mode = d.pop("commercial_mode", UNSET)
        commercial_mode: CommercialMode | Unset
        if isinstance(_commercial_mode, Unset):
            commercial_mode = UNSET
        else:
            commercial_mode = CommercialMode.from_dict(_commercial_mode)

        _line_groups = d.pop("line_groups", UNSET)
        line_groups: list[LineGroup] | Unset = UNSET
        if _line_groups is not UNSET:
            line_groups = []
            for line_groups_item_data in _line_groups:
                line_groups_item = LineGroup.from_dict(line_groups_item_data)

                line_groups.append(line_groups_item)

        line = cls(
            code=code,
            links=links,
            id=id,
            name=name,
            comment=comment,
            properties=properties,
            network=network,
            color=color,
            routes=routes,
            geojson=geojson,
            text_color=text_color,
            physical_modes=physical_modes,
            codes=codes,
            comments=comments,
            closing_time=closing_time,
            opening_time=opening_time,
            commercial_mode=commercial_mode,
            line_groups=line_groups,
        )

        line.additional_properties = d
        return line

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
