from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.section_additional_informations_item import SectionAdditionalInformationsItem
from ..models.section_data_freshness import SectionDataFreshness
from ..models.section_mode import SectionMode
from ..models.section_transfer_type import SectionTransferType
from ..models.section_type import SectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.journey import Journey
    from ..models.link_schema import LinkSchema
    from ..models.path import Path
    from ..models.place import Place
    from ..models.ridesharing_information import RidesharingInformation
    from ..models.section_geo_json_schema import SectionGeoJsonSchema
    from ..models.stop_date_time import StopDateTime
    from ..models.vj_display_information import VJDisplayInformation


T = TypeVar("T", bound="Section")


@_attrs_define
class Section:
    """
    Attributes:
        links (list[LinkSchema]):
        co2_emission (Amount):
        duration (int): Duration of the section (seconds)
        id (str):
        display_informations (VJDisplayInformation | Unset):
        from_ (Place | Unset):
        transfer_type (SectionTransferType | Unset):
        arrival_date_time (str | Unset): Arrival date and time of the section
        additional_informations (list[SectionAdditionalInformationsItem] | Unset):
        departure_date_time (str | Unset): Departure date and time of the section
        ridesharing_informations (RidesharingInformation | Unset):
        to (Place | Unset):
        base_arrival_date_time (str | Unset): Base-schedule arrival date and time of the section
        base_departure_date_time (str | Unset): Base-schedule departure date and time of the section
        ridesharing_journeys (list[Journey] | Unset):
        geojson (SectionGeoJsonSchema | Unset):
        path (list[Path] | Unset):
        stop_date_times (list[StopDateTime] | Unset):
        type_ (SectionType | Unset):
        data_freshness (SectionDataFreshness | Unset):
        mode (SectionMode | Unset):
    """

    links: list[LinkSchema]
    co2_emission: Amount
    duration: int
    id: str
    display_informations: VJDisplayInformation | Unset = UNSET
    from_: Place | Unset = UNSET
    transfer_type: SectionTransferType | Unset = UNSET
    arrival_date_time: str | Unset = UNSET
    additional_informations: list[SectionAdditionalInformationsItem] | Unset = UNSET
    departure_date_time: str | Unset = UNSET
    ridesharing_informations: RidesharingInformation | Unset = UNSET
    to: Place | Unset = UNSET
    base_arrival_date_time: str | Unset = UNSET
    base_departure_date_time: str | Unset = UNSET
    ridesharing_journeys: list[Journey] | Unset = UNSET
    geojson: SectionGeoJsonSchema | Unset = UNSET
    path: list[Path] | Unset = UNSET
    stop_date_times: list[StopDateTime] | Unset = UNSET
    type_: SectionType | Unset = UNSET
    data_freshness: SectionDataFreshness | Unset = UNSET
    mode: SectionMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        co2_emission = self.co2_emission.to_dict()

        duration = self.duration

        id = self.id

        display_informations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_informations, Unset):
            display_informations = self.display_informations.to_dict()

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        transfer_type: str | Unset = UNSET
        if not isinstance(self.transfer_type, Unset):
            transfer_type = self.transfer_type.value

        arrival_date_time = self.arrival_date_time

        additional_informations: list[str] | Unset = UNSET
        if not isinstance(self.additional_informations, Unset):
            additional_informations = []
            for additional_informations_item_data in self.additional_informations:
                additional_informations_item = additional_informations_item_data.value
                additional_informations.append(additional_informations_item)

        departure_date_time = self.departure_date_time

        ridesharing_informations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ridesharing_informations, Unset):
            ridesharing_informations = self.ridesharing_informations.to_dict()

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        base_arrival_date_time = self.base_arrival_date_time

        base_departure_date_time = self.base_departure_date_time

        ridesharing_journeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ridesharing_journeys, Unset):
            ridesharing_journeys = []
            for ridesharing_journeys_item_data in self.ridesharing_journeys:
                ridesharing_journeys_item = ridesharing_journeys_item_data.to_dict()
                ridesharing_journeys.append(ridesharing_journeys_item)

        geojson: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geojson, Unset):
            geojson = self.geojson.to_dict()

        path: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = []
            for path_item_data in self.path:
                path_item = path_item_data.to_dict()
                path.append(path_item)

        stop_date_times: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_date_times, Unset):
            stop_date_times = []
            for stop_date_times_item_data in self.stop_date_times:
                stop_date_times_item = stop_date_times_item_data.to_dict()
                stop_date_times.append(stop_date_times_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        data_freshness: str | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "co2_emission": co2_emission,
                "duration": duration,
                "id": id,
            }
        )
        if display_informations is not UNSET:
            field_dict["display_informations"] = display_informations
        if from_ is not UNSET:
            field_dict["from"] = from_
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type
        if arrival_date_time is not UNSET:
            field_dict["arrival_date_time"] = arrival_date_time
        if additional_informations is not UNSET:
            field_dict["additional_informations"] = additional_informations
        if departure_date_time is not UNSET:
            field_dict["departure_date_time"] = departure_date_time
        if ridesharing_informations is not UNSET:
            field_dict["ridesharing_informations"] = ridesharing_informations
        if to is not UNSET:
            field_dict["to"] = to
        if base_arrival_date_time is not UNSET:
            field_dict["base_arrival_date_time"] = base_arrival_date_time
        if base_departure_date_time is not UNSET:
            field_dict["base_departure_date_time"] = base_departure_date_time
        if ridesharing_journeys is not UNSET:
            field_dict["ridesharing_journeys"] = ridesharing_journeys
        if geojson is not UNSET:
            field_dict["geojson"] = geojson
        if path is not UNSET:
            field_dict["path"] = path
        if stop_date_times is not UNSET:
            field_dict["stop_date_times"] = stop_date_times
        if type_ is not UNSET:
            field_dict["type"] = type_
        if data_freshness is not UNSET:
            field_dict["data_freshness"] = data_freshness
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount
        from ..models.journey import Journey
        from ..models.link_schema import LinkSchema
        from ..models.path import Path
        from ..models.place import Place
        from ..models.ridesharing_information import RidesharingInformation
        from ..models.section_geo_json_schema import SectionGeoJsonSchema
        from ..models.stop_date_time import StopDateTime
        from ..models.vj_display_information import VJDisplayInformation

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        co2_emission = Amount.from_dict(d.pop("co2_emission"))

        duration = d.pop("duration")

        id = d.pop("id")

        _display_informations = d.pop("display_informations", UNSET)
        display_informations: VJDisplayInformation | Unset
        if isinstance(_display_informations, Unset):
            display_informations = UNSET
        else:
            display_informations = VJDisplayInformation.from_dict(_display_informations)

        _from_ = d.pop("from", UNSET)
        from_: Place | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Place.from_dict(_from_)

        _transfer_type = d.pop("transfer_type", UNSET)
        transfer_type: SectionTransferType | Unset
        if isinstance(_transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = SectionTransferType(_transfer_type)

        arrival_date_time = d.pop("arrival_date_time", UNSET)

        _additional_informations = d.pop("additional_informations", UNSET)
        additional_informations: list[SectionAdditionalInformationsItem] | Unset = UNSET
        if _additional_informations is not UNSET:
            additional_informations = []
            for additional_informations_item_data in _additional_informations:
                additional_informations_item = SectionAdditionalInformationsItem(additional_informations_item_data)

                additional_informations.append(additional_informations_item)

        departure_date_time = d.pop("departure_date_time", UNSET)

        _ridesharing_informations = d.pop("ridesharing_informations", UNSET)
        ridesharing_informations: RidesharingInformation | Unset
        if isinstance(_ridesharing_informations, Unset):
            ridesharing_informations = UNSET
        else:
            ridesharing_informations = RidesharingInformation.from_dict(_ridesharing_informations)

        _to = d.pop("to", UNSET)
        to: Place | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Place.from_dict(_to)

        base_arrival_date_time = d.pop("base_arrival_date_time", UNSET)

        base_departure_date_time = d.pop("base_departure_date_time", UNSET)

        _ridesharing_journeys = d.pop("ridesharing_journeys", UNSET)
        ridesharing_journeys: list[Journey] | Unset = UNSET
        if _ridesharing_journeys is not UNSET:
            ridesharing_journeys = []
            for ridesharing_journeys_item_data in _ridesharing_journeys:
                ridesharing_journeys_item = Journey.from_dict(ridesharing_journeys_item_data)

                ridesharing_journeys.append(ridesharing_journeys_item)

        _geojson = d.pop("geojson", UNSET)
        geojson: SectionGeoJsonSchema | Unset
        if isinstance(_geojson, Unset):
            geojson = UNSET
        else:
            geojson = SectionGeoJsonSchema.from_dict(_geojson)

        _path = d.pop("path", UNSET)
        path: list[Path] | Unset = UNSET
        if _path is not UNSET:
            path = []
            for path_item_data in _path:
                path_item = Path.from_dict(path_item_data)

                path.append(path_item)

        _stop_date_times = d.pop("stop_date_times", UNSET)
        stop_date_times: list[StopDateTime] | Unset = UNSET
        if _stop_date_times is not UNSET:
            stop_date_times = []
            for stop_date_times_item_data in _stop_date_times:
                stop_date_times_item = StopDateTime.from_dict(stop_date_times_item_data)

                stop_date_times.append(stop_date_times_item)

        _type_ = d.pop("type", UNSET)
        type_: SectionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SectionType(_type_)

        _data_freshness = d.pop("data_freshness", UNSET)
        data_freshness: SectionDataFreshness | Unset
        if isinstance(_data_freshness, Unset):
            data_freshness = UNSET
        else:
            data_freshness = SectionDataFreshness(_data_freshness)

        _mode = d.pop("mode", UNSET)
        mode: SectionMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SectionMode(_mode)

        section = cls(
            links=links,
            co2_emission=co2_emission,
            duration=duration,
            id=id,
            display_informations=display_informations,
            from_=from_,
            transfer_type=transfer_type,
            arrival_date_time=arrival_date_time,
            additional_informations=additional_informations,
            departure_date_time=departure_date_time,
            ridesharing_informations=ridesharing_informations,
            to=to,
            base_arrival_date_time=base_arrival_date_time,
            base_departure_date_time=base_departure_date_time,
            ridesharing_journeys=ridesharing_journeys,
            geojson=geojson,
            path=path,
            stop_date_times=stop_date_times,
            type_=type_,
            data_freshness=data_freshness,
            mode=mode,
        )

        section.additional_properties = d
        return section

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
