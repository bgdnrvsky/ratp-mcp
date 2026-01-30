from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.place_nearby_embedded_type import PlaceNearbyEmbeddedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.admin import Admin
    from ..models.poi import Poi
    from ..models.stop_area import StopArea
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="PlaceNearby")


@_attrs_define
class PlaceNearby:
    embedded_type: PlaceNearbyEmbeddedType
    name: str
    """ Name of the object """
    id: str
    """ Identifier of the object """
    stop_point: StopPoint | Unset = UNSET
    administrative_region: Admin | Unset = UNSET
    distance: str | Unset = UNSET
    """ Distance to the object in meters """
    poi: Poi | Unset = UNSET
    address: Address | Unset = UNSET
    quality: int | Unset = UNSET
    stop_area: StopArea | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedded_type = self.embedded_type.value

        name = self.name

        id = self.id

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        administrative_region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.administrative_region, Unset):
            administrative_region = self.administrative_region.to_dict()

        distance = self.distance

        poi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poi, Unset):
            poi = self.poi.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        quality = self.quality

        stop_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_area, Unset):
            stop_area = self.stop_area.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embedded_type": embedded_type,
                "name": name,
                "id": id,
            }
        )
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if administrative_region is not UNSET:
            field_dict["administrative_region"] = administrative_region
        if distance is not UNSET:
            field_dict["distance"] = distance
        if poi is not UNSET:
            field_dict["poi"] = poi
        if address is not UNSET:
            field_dict["address"] = address
        if quality is not UNSET:
            field_dict["quality"] = quality
        if stop_area is not UNSET:
            field_dict["stop_area"] = stop_area

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.admin import Admin
        from ..models.poi import Poi
        from ..models.stop_area import StopArea
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        embedded_type = PlaceNearbyEmbeddedType(d.pop("embedded_type"))

        name = d.pop("name")

        id = d.pop("id")

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        _administrative_region = d.pop("administrative_region", UNSET)
        administrative_region: Admin | Unset
        if isinstance(_administrative_region, Unset):
            administrative_region = UNSET
        else:
            administrative_region = Admin.from_dict(_administrative_region)

        distance = d.pop("distance", UNSET)

        _poi = d.pop("poi", UNSET)
        poi: Poi | Unset
        if isinstance(_poi, Unset):
            poi = UNSET
        else:
            poi = Poi.from_dict(_poi)

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        quality = d.pop("quality", UNSET)

        _stop_area = d.pop("stop_area", UNSET)
        stop_area: StopArea | Unset
        if isinstance(_stop_area, Unset):
            stop_area = UNSET
        else:
            stop_area = StopArea.from_dict(_stop_area)

        place_nearby = cls(
            embedded_type=embedded_type,
            name=name,
            id=id,
            stop_point=stop_point,
            administrative_region=administrative_region,
            distance=distance,
            poi=poi,
            address=address,
            quality=quality,
            stop_area=stop_area,
        )

        place_nearby.additional_properties = d
        return place_nearby

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
