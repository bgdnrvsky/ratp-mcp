from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount
    from ..models.calendar import Calendar
    from ..models.distances import Distances
    from ..models.durations import Durations
    from ..models.fare import Fare
    from ..models.journey_debug import JourneyDebug
    from ..models.link_schema import LinkSchema
    from ..models.place import Place
    from ..models.section import Section


T = TypeVar("T", bound="Journey")


@_attrs_define
class Journey:
    status: str
    """ Status from the whole journey taking into account the most disturbing information retrieved on every object
    used (can be "NO_SERVICE", "SIGNIFICANT_DELAYS", ... """
    tags: list[str]
    nb_transfers: int
    """ Number of transfers along the journey """
    fare: Fare
    co2_emission: Amount
    type_: str
    """ Used to qualify the journey (can be "best", "comfort", "non_pt_walk", ... """
    duration: int
    """ Duration of the journey (seconds) """
    distances: Distances | Unset = UNSET
    from_: Place | Unset = UNSET
    links: list[LinkSchema] | Unset = UNSET
    durations: Durations | Unset = UNSET
    arrival_date_time: str | Unset = UNSET
    """ Arrival date and time of the journey """
    calendars: list[Calendar] | Unset = UNSET
    departure_date_time: str | Unset = UNSET
    """ Departure date and time of the journey """
    to: Place | Unset = UNSET
    requested_date_time: str | Unset = UNSET
    sections: list[Section] | Unset = UNSET
    debug: JourneyDebug | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        tags = self.tags

        nb_transfers = self.nb_transfers

        fare = self.fare.to_dict()

        co2_emission = self.co2_emission.to_dict()

        type_ = self.type_

        duration = self.duration

        distances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distances, Unset):
            distances = self.distances.to_dict()

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        durations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.durations, Unset):
            durations = self.durations.to_dict()

        arrival_date_time = self.arrival_date_time

        calendars: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = []
            for calendars_item_data in self.calendars:
                calendars_item = calendars_item_data.to_dict()
                calendars.append(calendars_item)

        departure_date_time = self.departure_date_time

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        requested_date_time = self.requested_date_time

        sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "tags": tags,
                "nb_transfers": nb_transfers,
                "fare": fare,
                "co2_emission": co2_emission,
                "type": type_,
                "duration": duration,
            }
        )
        if distances is not UNSET:
            field_dict["distances"] = distances
        if from_ is not UNSET:
            field_dict["from"] = from_
        if links is not UNSET:
            field_dict["links"] = links
        if durations is not UNSET:
            field_dict["durations"] = durations
        if arrival_date_time is not UNSET:
            field_dict["arrival_date_time"] = arrival_date_time
        if calendars is not UNSET:
            field_dict["calendars"] = calendars
        if departure_date_time is not UNSET:
            field_dict["departure_date_time"] = departure_date_time
        if to is not UNSET:
            field_dict["to"] = to
        if requested_date_time is not UNSET:
            field_dict["requested_date_time"] = requested_date_time
        if sections is not UNSET:
            field_dict["sections"] = sections
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount
        from ..models.calendar import Calendar
        from ..models.distances import Distances
        from ..models.durations import Durations
        from ..models.fare import Fare
        from ..models.journey_debug import JourneyDebug
        from ..models.link_schema import LinkSchema
        from ..models.place import Place
        from ..models.section import Section

        d = dict(src_dict)
        status = d.pop("status")

        tags = cast(list[str], d.pop("tags"))

        nb_transfers = d.pop("nb_transfers")

        fare = Fare.from_dict(d.pop("fare"))

        co2_emission = Amount.from_dict(d.pop("co2_emission"))

        type_ = d.pop("type")

        duration = d.pop("duration")

        _distances = d.pop("distances", UNSET)
        distances: Distances | Unset
        if isinstance(_distances, Unset):
            distances = UNSET
        else:
            distances = Distances.from_dict(_distances)

        _from_ = d.pop("from", UNSET)
        from_: Place | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Place.from_dict(_from_)

        _links = d.pop("links", UNSET)
        links: list[LinkSchema] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = LinkSchema.from_dict(links_item_data)

                links.append(links_item)

        _durations = d.pop("durations", UNSET)
        durations: Durations | Unset
        if isinstance(_durations, Unset):
            durations = UNSET
        else:
            durations = Durations.from_dict(_durations)

        arrival_date_time = d.pop("arrival_date_time", UNSET)

        _calendars = d.pop("calendars", UNSET)
        calendars: list[Calendar] | Unset = UNSET
        if _calendars is not UNSET:
            calendars = []
            for calendars_item_data in _calendars:
                calendars_item = Calendar.from_dict(calendars_item_data)

                calendars.append(calendars_item)

        departure_date_time = d.pop("departure_date_time", UNSET)

        _to = d.pop("to", UNSET)
        to: Place | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Place.from_dict(_to)

        requested_date_time = d.pop("requested_date_time", UNSET)

        _sections = d.pop("sections", UNSET)
        sections: list[Section] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = Section.from_dict(sections_item_data)

                sections.append(sections_item)

        _debug = d.pop("debug", UNSET)
        debug: JourneyDebug | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = JourneyDebug.from_dict(_debug)

        journey = cls(
            status=status,
            tags=tags,
            nb_transfers=nb_transfers,
            fare=fare,
            co2_emission=co2_emission,
            type_=type_,
            duration=duration,
            distances=distances,
            from_=from_,
            links=links,
            durations=durations,
            arrival_date_time=arrival_date_time,
            calendars=calendars,
            departure_date_time=departure_date_time,
            to=to,
            requested_date_time=requested_date_time,
            sections=sections,
            debug=debug,
        )

        journey.additional_properties = d
        return journey

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
