from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vj_display_information_equipments_item import VJDisplayInformationEquipmentsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema


T = TypeVar("T", bound="VJDisplayInformation")


@_attrs_define
class VJDisplayInformation:
    """
    Attributes:
        direction (str):
        links (list[LinkSchema]):
        headsign (str):
        equipments (list[VJDisplayInformationEquipmentsItem]):
        code (str | Unset):
        network (str | Unset):
        color (str | Unset):
        name (str | Unset):
        physical_mode (str | Unset):
        label (str | Unset):
        text_color (str | Unset):
        headsigns (list[str] | Unset):
        commercial_mode (str | Unset):
        description (str | Unset):
    """

    direction: str
    links: list[LinkSchema]
    headsign: str
    equipments: list[VJDisplayInformationEquipmentsItem]
    code: str | Unset = UNSET
    network: str | Unset = UNSET
    color: str | Unset = UNSET
    name: str | Unset = UNSET
    physical_mode: str | Unset = UNSET
    label: str | Unset = UNSET
    text_color: str | Unset = UNSET
    headsigns: list[str] | Unset = UNSET
    commercial_mode: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        headsign = self.headsign

        equipments = []
        for equipments_item_data in self.equipments:
            equipments_item = equipments_item_data.value
            equipments.append(equipments_item)

        code = self.code

        network = self.network

        color = self.color

        name = self.name

        physical_mode = self.physical_mode

        label = self.label

        text_color = self.text_color

        headsigns: list[str] | Unset = UNSET
        if not isinstance(self.headsigns, Unset):
            headsigns = self.headsigns

        commercial_mode = self.commercial_mode

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "direction": direction,
                "links": links,
                "headsign": headsign,
                "equipments": equipments,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if network is not UNSET:
            field_dict["network"] = network
        if color is not UNSET:
            field_dict["color"] = color
        if name is not UNSET:
            field_dict["name"] = name
        if physical_mode is not UNSET:
            field_dict["physical_mode"] = physical_mode
        if label is not UNSET:
            field_dict["label"] = label
        if text_color is not UNSET:
            field_dict["text_color"] = text_color
        if headsigns is not UNSET:
            field_dict["headsigns"] = headsigns
        if commercial_mode is not UNSET:
            field_dict["commercial_mode"] = commercial_mode
        if description is not UNSET:
            field_dict["description"] = description

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

        headsign = d.pop("headsign")

        equipments = []
        _equipments = d.pop("equipments")
        for equipments_item_data in _equipments:
            equipments_item = VJDisplayInformationEquipmentsItem(equipments_item_data)

            equipments.append(equipments_item)

        code = d.pop("code", UNSET)

        network = d.pop("network", UNSET)

        color = d.pop("color", UNSET)

        name = d.pop("name", UNSET)

        physical_mode = d.pop("physical_mode", UNSET)

        label = d.pop("label", UNSET)

        text_color = d.pop("text_color", UNSET)

        headsigns = cast(list[str], d.pop("headsigns", UNSET))

        commercial_mode = d.pop("commercial_mode", UNSET)

        description = d.pop("description", UNSET)

        vj_display_information = cls(
            direction=direction,
            links=links,
            headsign=headsign,
            equipments=equipments,
            code=code,
            network=network,
            color=color,
            name=name,
            physical_mode=physical_mode,
            label=label,
            text_color=text_color,
            headsigns=headsigns,
            commercial_mode=commercial_mode,
            description=description,
        )

        vj_display_information.additional_properties = d
        return vj_display_information

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
