from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_date_time_additional_informations_item import StopDateTimeAdditionalInformationsItem
from ..models.stop_date_time_data_freshness import StopDateTimeDataFreshness
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema
    from ..models.stop_point import StopPoint


T = TypeVar("T", bound="StopDateTime")


@_attrs_define
class StopDateTime:
    links: list[LinkSchema]
    additional_informations: list[StopDateTimeAdditionalInformationsItem]
    stop_point: StopPoint | Unset = UNSET
    arrival_date_time: str | Unset = UNSET
    departure_date_time: str | Unset = UNSET
    base_arrival_date_time: str | Unset = UNSET
    base_departure_date_time: str | Unset = UNSET
    data_freshness: StopDateTimeDataFreshness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        additional_informations = []
        for additional_informations_item_data in self.additional_informations:
            additional_informations_item = additional_informations_item_data.value
            additional_informations.append(additional_informations_item)

        stop_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stop_point, Unset):
            stop_point = self.stop_point.to_dict()

        arrival_date_time = self.arrival_date_time

        departure_date_time = self.departure_date_time

        base_arrival_date_time = self.base_arrival_date_time

        base_departure_date_time = self.base_departure_date_time

        data_freshness: str | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "additional_informations": additional_informations,
            }
        )
        if stop_point is not UNSET:
            field_dict["stop_point"] = stop_point
        if arrival_date_time is not UNSET:
            field_dict["arrival_date_time"] = arrival_date_time
        if departure_date_time is not UNSET:
            field_dict["departure_date_time"] = departure_date_time
        if base_arrival_date_time is not UNSET:
            field_dict["base_arrival_date_time"] = base_arrival_date_time
        if base_departure_date_time is not UNSET:
            field_dict["base_departure_date_time"] = base_departure_date_time
        if data_freshness is not UNSET:
            field_dict["data_freshness"] = data_freshness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_schema import LinkSchema
        from ..models.stop_point import StopPoint

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        additional_informations = []
        _additional_informations = d.pop("additional_informations")
        for additional_informations_item_data in _additional_informations:
            additional_informations_item = StopDateTimeAdditionalInformationsItem(additional_informations_item_data)

            additional_informations.append(additional_informations_item)

        _stop_point = d.pop("stop_point", UNSET)
        stop_point: StopPoint | Unset
        if isinstance(_stop_point, Unset):
            stop_point = UNSET
        else:
            stop_point = StopPoint.from_dict(_stop_point)

        arrival_date_time = d.pop("arrival_date_time", UNSET)

        departure_date_time = d.pop("departure_date_time", UNSET)

        base_arrival_date_time = d.pop("base_arrival_date_time", UNSET)

        base_departure_date_time = d.pop("base_departure_date_time", UNSET)

        _data_freshness = d.pop("data_freshness", UNSET)
        data_freshness: StopDateTimeDataFreshness | Unset
        if isinstance(_data_freshness, Unset):
            data_freshness = UNSET
        else:
            data_freshness = StopDateTimeDataFreshness(_data_freshness)

        stop_date_time = cls(
            links=links,
            additional_informations=additional_informations,
            stop_point=stop_point,
            arrival_date_time=arrival_date_time,
            departure_date_time=departure_date_time,
            base_arrival_date_time=base_arrival_date_time,
            base_departure_date_time=base_departure_date_time,
            data_freshness=data_freshness,
        )

        stop_date_time.additional_properties = d
        return stop_date_time

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
