from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_point_equipments_item import StopPointEquipmentsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.admin import Admin
    from ..models.code import Code
    from ..models.comment import Comment
    from ..models.commercial_mode import CommercialMode
    from ..models.coord import Coord
    from ..models.equipment_details import EquipmentDetails
    from ..models.fare_zone import FareZone
    from ..models.link_schema import LinkSchema
    from ..models.physical_mode import PhysicalMode
    from ..models.stop_area import StopArea


T = TypeVar("T", bound="StopPoint")


@_attrs_define
class StopPoint:
    """
    Attributes:
        links (list[LinkSchema]):
        equipments (list[StopPointEquipmentsItem]):
        id (str): Identifier of the object
        name (str): Name of the object
        comment (str | Unset):
        commercial_modes (list[CommercialMode] | Unset):
        stop_area (StopArea | Unset):
        administrative_regions (list[Admin] | Unset):
        physical_modes (list[PhysicalMode] | Unset):
        comments (list[Comment] | Unset):
        label (str | Unset):
        codes (list[Code] | Unset):
        coord (Coord | Unset):
        equipment_details (list[EquipmentDetails] | Unset):
        address (Address | Unset):
        fare_zone (FareZone | Unset):
    """

    links: list[LinkSchema]
    equipments: list[StopPointEquipmentsItem]
    id: str
    name: str
    comment: str | Unset = UNSET
    commercial_modes: list[CommercialMode] | Unset = UNSET
    stop_area: StopArea | Unset = UNSET
    administrative_regions: list[Admin] | Unset = UNSET
    physical_modes: list[PhysicalMode] | Unset = UNSET
    comments: list[Comment] | Unset = UNSET
    label: str | Unset = UNSET
    codes: list[Code] | Unset = UNSET
    coord: Coord | Unset = UNSET
    equipment_details: list[EquipmentDetails] | Unset = UNSET
    address: Address | Unset = UNSET
    fare_zone: FareZone | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        equipments = []
        for equipments_item_data in self.equipments:
            equipments_item = equipments_item_data.value
            equipments.append(equipments_item)

        id = self.id

        name = self.name

        comment = self.comment

        commercial_modes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.commercial_modes, Unset):
            commercial_modes = []
            for commercial_modes_item_data in self.commercial_modes:
                commercial_modes_item = commercial_modes_item_data.to_dict()
                commercial_modes.append(commercial_modes_item)

        stop_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_area, Unset):
            stop_area = self.stop_area.to_dict()

        administrative_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.administrative_regions, Unset):
            administrative_regions = []
            for administrative_regions_item_data in self.administrative_regions:
                administrative_regions_item = administrative_regions_item_data.to_dict()
                administrative_regions.append(administrative_regions_item)

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

        codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()
                codes.append(codes_item)

        coord: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coord, Unset):
            coord = self.coord.to_dict()

        equipment_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.equipment_details, Unset):
            equipment_details = []
            for equipment_details_item_data in self.equipment_details:
                equipment_details_item = equipment_details_item_data.to_dict()
                equipment_details.append(equipment_details_item)

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        fare_zone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fare_zone, Unset):
            fare_zone = self.fare_zone.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "equipments": equipments,
                "id": id,
                "name": name,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if commercial_modes is not UNSET:
            field_dict["commercial_modes"] = commercial_modes
        if stop_area is not UNSET:
            field_dict["stop_area"] = stop_area
        if administrative_regions is not UNSET:
            field_dict["administrative_regions"] = administrative_regions
        if physical_modes is not UNSET:
            field_dict["physical_modes"] = physical_modes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if label is not UNSET:
            field_dict["label"] = label
        if codes is not UNSET:
            field_dict["codes"] = codes
        if coord is not UNSET:
            field_dict["coord"] = coord
        if equipment_details is not UNSET:
            field_dict["equipment_details"] = equipment_details
        if address is not UNSET:
            field_dict["address"] = address
        if fare_zone is not UNSET:
            field_dict["fare_zone"] = fare_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.admin import Admin
        from ..models.code import Code
        from ..models.comment import Comment
        from ..models.commercial_mode import CommercialMode
        from ..models.coord import Coord
        from ..models.equipment_details import EquipmentDetails
        from ..models.fare_zone import FareZone
        from ..models.link_schema import LinkSchema
        from ..models.physical_mode import PhysicalMode
        from ..models.stop_area import StopArea

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        equipments = []
        _equipments = d.pop("equipments")
        for equipments_item_data in _equipments:
            equipments_item = StopPointEquipmentsItem(equipments_item_data)

            equipments.append(equipments_item)

        id = d.pop("id")

        name = d.pop("name")

        comment = d.pop("comment", UNSET)

        _commercial_modes = d.pop("commercial_modes", UNSET)
        commercial_modes: list[CommercialMode] | Unset = UNSET
        if _commercial_modes is not UNSET:
            commercial_modes = []
            for commercial_modes_item_data in _commercial_modes:
                commercial_modes_item = CommercialMode.from_dict(commercial_modes_item_data)

                commercial_modes.append(commercial_modes_item)

        _stop_area = d.pop("stop_area", UNSET)
        stop_area: StopArea | Unset
        if isinstance(_stop_area, Unset):
            stop_area = UNSET
        else:
            stop_area = StopArea.from_dict(_stop_area)

        _administrative_regions = d.pop("administrative_regions", UNSET)
        administrative_regions: list[Admin] | Unset = UNSET
        if _administrative_regions is not UNSET:
            administrative_regions = []
            for administrative_regions_item_data in _administrative_regions:
                administrative_regions_item = Admin.from_dict(administrative_regions_item_data)

                administrative_regions.append(administrative_regions_item)

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

        _codes = d.pop("codes", UNSET)
        codes: list[Code] | Unset = UNSET
        if _codes is not UNSET:
            codes = []
            for codes_item_data in _codes:
                codes_item = Code.from_dict(codes_item_data)

                codes.append(codes_item)

        _coord = d.pop("coord", UNSET)
        coord: Coord | Unset
        if isinstance(_coord, Unset):
            coord = UNSET
        else:
            coord = Coord.from_dict(_coord)

        _equipment_details = d.pop("equipment_details", UNSET)
        equipment_details: list[EquipmentDetails] | Unset = UNSET
        if _equipment_details is not UNSET:
            equipment_details = []
            for equipment_details_item_data in _equipment_details:
                equipment_details_item = EquipmentDetails.from_dict(equipment_details_item_data)

                equipment_details.append(equipment_details_item)

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _fare_zone = d.pop("fare_zone", UNSET)
        fare_zone: FareZone | Unset
        if isinstance(_fare_zone, Unset):
            fare_zone = UNSET
        else:
            fare_zone = FareZone.from_dict(_fare_zone)

        stop_point = cls(
            links=links,
            equipments=equipments,
            id=id,
            name=name,
            comment=comment,
            commercial_modes=commercial_modes,
            stop_area=stop_area,
            administrative_regions=administrative_regions,
            physical_modes=physical_modes,
            comments=comments,
            label=label,
            codes=codes,
            coord=coord,
            equipment_details=equipment_details,
            address=address,
            fare_zone=fare_zone,
        )

        stop_point.additional_properties = d
        return stop_point

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
