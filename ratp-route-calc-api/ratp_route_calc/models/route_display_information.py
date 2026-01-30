from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema


T = TypeVar("T", bound="RouteDisplayInformation")


@_attrs_define
class RouteDisplayInformation:
    direction: str
    links: list[LinkSchema]
    code: str | Unset = UNSET
    network: str | Unset = UNSET
    color: str | Unset = UNSET
    label: str | Unset = UNSET
    commercial_mode: str | Unset = UNSET
    text_color: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        code = self.code

        network = self.network

        color = self.color

        label = self.label

        commercial_mode = self.commercial_mode

        text_color = self.text_color

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "links": links,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if network is not UNSET:
            field_dict["network"] = network
        if color is not UNSET:
            field_dict["color"] = color
        if label is not UNSET:
            field_dict["label"] = label
        if commercial_mode is not UNSET:
            field_dict["commercial_mode"] = commercial_mode
        if text_color is not UNSET:
            field_dict["text_color"] = text_color
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_schema import LinkSchema

        d = dict(src_dict)
        direction = d.pop("direction")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        code = d.pop("code", UNSET)

        network = d.pop("network", UNSET)

        color = d.pop("color", UNSET)

        label = d.pop("label", UNSET)

        commercial_mode = d.pop("commercial_mode", UNSET)

        text_color = d.pop("text_color", UNSET)

        name = d.pop("name", UNSET)

        route_display_information = cls(
            direction=direction,
            links=links,
            code=code,
            network=network,
            color=color,
            label=label,
            commercial_mode=commercial_mode,
            text_color=text_color,
            name=name,
        )

        route_display_information.additional_properties = d
        return route_display_information

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
