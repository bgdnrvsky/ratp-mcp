from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line import Line
    from ..models.network import Network
    from ..models.stop_area import StopArea
    from ..models.vehicle_journey import VehicleJourney


T = TypeVar("T", bound="TrafficReport")


@_attrs_define
class TrafficReport:
    vehicle_journeys: list[VehicleJourney] | Unset = UNSET
    lines: list[Line] | Unset = UNSET
    network: Network | Unset = UNSET
    stop_areas: list[StopArea] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vehicle_journeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vehicle_journeys, Unset):
            vehicle_journeys = []
            for vehicle_journeys_item_data in self.vehicle_journeys:
                vehicle_journeys_item = vehicle_journeys_item_data.to_dict()
                vehicle_journeys.append(vehicle_journeys_item)

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        stop_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_areas, Unset):
            stop_areas = []
            for stop_areas_item_data in self.stop_areas:
                stop_areas_item = stop_areas_item_data.to_dict()
                stop_areas.append(stop_areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vehicle_journeys is not UNSET:
            field_dict["vehicle_journeys"] = vehicle_journeys
        if lines is not UNSET:
            field_dict["lines"] = lines
        if network is not UNSET:
            field_dict["network"] = network
        if stop_areas is not UNSET:
            field_dict["stop_areas"] = stop_areas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line import Line
        from ..models.network import Network
        from ..models.stop_area import StopArea
        from ..models.vehicle_journey import VehicleJourney

        d = dict(src_dict)
        _vehicle_journeys = d.pop("vehicle_journeys", UNSET)
        vehicle_journeys: list[VehicleJourney] | Unset = UNSET
        if _vehicle_journeys is not UNSET:
            vehicle_journeys = []
            for vehicle_journeys_item_data in _vehicle_journeys:
                vehicle_journeys_item = VehicleJourney.from_dict(vehicle_journeys_item_data)

                vehicle_journeys.append(vehicle_journeys_item)

        _lines = d.pop("lines", UNSET)
        lines: list[Line] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = Line.from_dict(lines_item_data)

                lines.append(lines_item)

        _network = d.pop("network", UNSET)
        network: Network | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = Network.from_dict(_network)

        _stop_areas = d.pop("stop_areas", UNSET)
        stop_areas: list[StopArea] | Unset = UNSET
        if _stop_areas is not UNSET:
            stop_areas = []
            for stop_areas_item_data in _stop_areas:
                stop_areas_item = StopArea.from_dict(stop_areas_item_data)

                stop_areas.append(stop_areas_item)

        traffic_report = cls(
            vehicle_journeys=vehicle_journeys,
            lines=lines,
            network=network,
            stop_areas=stop_areas,
        )

        traffic_report.additional_properties = d
        return traffic_report

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
