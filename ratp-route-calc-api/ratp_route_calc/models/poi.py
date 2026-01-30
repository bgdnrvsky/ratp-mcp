from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.admin import Admin
    from ..models.car_park import CarPark
    from ..models.coord import Coord
    from ..models.poi_properties import PoiProperties
    from ..models.poi_type import PoiType
    from ..models.stands import Stands


T = TypeVar("T", bound="Poi")


@_attrs_define
class Poi:
    name: str
    """ Name of the object """
    id: str
    """ Identifier of the object """
    poi_type: PoiType | Unset = UNSET
    car_park: CarPark | Unset = UNSET
    coord: Coord | Unset = UNSET
    label: str | Unset = UNSET
    administrative_regions: list[Admin] | Unset = UNSET
    address: Address | Unset = UNSET
    properties: PoiProperties | Unset = UNSET
    stands: Stands | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        poi_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poi_type, Unset):
            poi_type = self.poi_type.to_dict()

        car_park: dict[str, Any] | Unset = UNSET
        if not isinstance(self.car_park, Unset):
            car_park = self.car_park.to_dict()

        coord: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coord, Unset):
            coord = self.coord.to_dict()

        label = self.label

        administrative_regions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.administrative_regions, Unset):
            administrative_regions = []
            for administrative_regions_item_data in self.administrative_regions:
                administrative_regions_item = administrative_regions_item_data.to_dict()
                administrative_regions.append(administrative_regions_item)

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        stands: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stands, Unset):
            stands = self.stands.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
            }
        )
        if poi_type is not UNSET:
            field_dict["poi_type"] = poi_type
        if car_park is not UNSET:
            field_dict["car_park"] = car_park
        if coord is not UNSET:
            field_dict["coord"] = coord
        if label is not UNSET:
            field_dict["label"] = label
        if administrative_regions is not UNSET:
            field_dict["administrative_regions"] = administrative_regions
        if address is not UNSET:
            field_dict["address"] = address
        if properties is not UNSET:
            field_dict["properties"] = properties
        if stands is not UNSET:
            field_dict["stands"] = stands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.admin import Admin
        from ..models.car_park import CarPark
        from ..models.coord import Coord
        from ..models.poi_properties import PoiProperties
        from ..models.poi_type import PoiType
        from ..models.stands import Stands

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id")

        _poi_type = d.pop("poi_type", UNSET)
        poi_type: PoiType | Unset
        if isinstance(_poi_type, Unset):
            poi_type = UNSET
        else:
            poi_type = PoiType.from_dict(_poi_type)

        _car_park = d.pop("car_park", UNSET)
        car_park: CarPark | Unset
        if isinstance(_car_park, Unset):
            car_park = UNSET
        else:
            car_park = CarPark.from_dict(_car_park)

        _coord = d.pop("coord", UNSET)
        coord: Coord | Unset
        if isinstance(_coord, Unset):
            coord = UNSET
        else:
            coord = Coord.from_dict(_coord)

        label = d.pop("label", UNSET)

        _administrative_regions = d.pop("administrative_regions", UNSET)
        administrative_regions: list[Admin] | Unset = UNSET
        if _administrative_regions is not UNSET:
            administrative_regions = []
            for administrative_regions_item_data in _administrative_regions:
                administrative_regions_item = Admin.from_dict(administrative_regions_item_data)

                administrative_regions.append(administrative_regions_item)

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        _properties = d.pop("properties", UNSET)
        properties: PoiProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PoiProperties.from_dict(_properties)

        _stands = d.pop("stands", UNSET)
        stands: Stands | Unset
        if isinstance(_stands, Unset):
            stands = UNSET
        else:
            stands = Stands.from_dict(_stands)

        poi = cls(
            name=name,
            id=id,
            poi_type=poi_type,
            car_park=car_park,
            coord=coord,
            label=label,
            administrative_regions=administrative_regions,
            address=address,
            properties=properties,
            stands=stands,
        )

        poi.additional_properties = d
        return poi

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
