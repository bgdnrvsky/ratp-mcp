from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pt_object_embedded_type import PtObjectEmbeddedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commercial_mode import CommercialMode
    from ..models.line import Line
    from ..models.network import Network
    from ..models.route import Route
    from ..models.stop_area import StopArea
    from ..models.stop_point import StopPoint
    from ..models.trip import Trip


T = TypeVar("T", bound="PtObject")


@_attrs_define
class PtObject:
    """
    Attributes:
        embedded_type (PtObjectEmbeddedType):
        name (str): Name of the object
        id (str): Identifier of the object
        stop_point (StopPoint | Unset):
        route (Route | Unset):
        stop_area (StopArea | Unset):
        commercial_mode (CommercialMode | Unset):
        line (Line | Unset):
        quality (int | Unset):
        trip (Trip | Unset):
        network (Network | Unset):
    """

    embedded_type: PtObjectEmbeddedType
    name: str
    id: str
    stop_point: StopPoint | Unset = UNSET
    route: Route | Unset = UNSET
    stop_area: StopArea | Unset = UNSET
    commercial_mode: CommercialMode | Unset = UNSET
    line: Line | Unset = UNSET
    quality: int | Unset = UNSET
    trip: Trip | Unset = UNSET
    network: Network | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embedded_type = self.embedded_type.value

        name = self.name

        id = self.id

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        route: dict[str, Any] | Unset = UNSET
        if not isinstance(self.route, Unset):
            route = self.route.to_dict()

        stop_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_area, Unset):
            stop_area = self.stop_area.to_dict()

        commercial_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commercial_mode, Unset):
            commercial_mode = self.commercial_mode.to_dict()

        line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line, Unset):
            line = self.line.to_dict()

        quality = self.quality

        trip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trip, Unset):
            trip = self.trip.to_dict()

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

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
        if route is not UNSET:
            field_dict["route"] = route
        if stop_area is not UNSET:
            field_dict["stop_area"] = stop_area
        if commercial_mode is not UNSET:
            field_dict["commercial_mode"] = commercial_mode
        if line is not UNSET:
            field_dict["line"] = line
        if quality is not UNSET:
            field_dict["quality"] = quality
        if trip is not UNSET:
            field_dict["trip"] = trip
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commercial_mode import CommercialMode
        from ..models.line import Line
        from ..models.network import Network
        from ..models.route import Route
        from ..models.stop_area import StopArea
        from ..models.stop_point import StopPoint
        from ..models.trip import Trip

        d = dict(src_dict)
        embedded_type = PtObjectEmbeddedType(d.pop("embedded_type"))

        name = d.pop("name")

        id = d.pop("id")

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        _route = d.pop("route", UNSET)
        route: Route | Unset
        if isinstance(_route, Unset):
            route = UNSET
        else:
            route = Route.from_dict(_route)

        _stop_area = d.pop("stop_area", UNSET)
        stop_area: StopArea | Unset
        if isinstance(_stop_area, Unset):
            stop_area = UNSET
        else:
            stop_area = StopArea.from_dict(_stop_area)

        _commercial_mode = d.pop("commercial_mode", UNSET)
        commercial_mode: CommercialMode | Unset
        if isinstance(_commercial_mode, Unset):
            commercial_mode = UNSET
        else:
            commercial_mode = CommercialMode.from_dict(_commercial_mode)

        _line = d.pop("line", UNSET)
        line: Line | Unset
        if isinstance(_line, Unset):
            line = UNSET
        else:
            line = Line.from_dict(_line)

        quality = d.pop("quality", UNSET)

        _trip = d.pop("trip", UNSET)
        trip: Trip | Unset
        if isinstance(_trip, Unset):
            trip = UNSET
        else:
            trip = Trip.from_dict(_trip)

        _network = d.pop("network", UNSET)
        network: Network | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = Network.from_dict(_network)

        pt_object = cls(
            embedded_type=embedded_type,
            name=name,
            id=id,
            stop_point=stop_point,
            route=route,
            stop_area=stop_area,
            commercial_mode=commercial_mode,
            line=line,
            quality=quality,
            trip=trip,
            network=network,
        )

        pt_object.additional_properties = d
        return pt_object

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
