from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.calendar import Calendar
    from ..models.code import Code
    from ..models.comment import Comment
    from ..models.journey_pattern import JourneyPattern
    from ..models.link_schema import LinkSchema
    from ..models.stop_time import StopTime
    from ..models.trip import Trip
    from ..models.validity_pattern import ValidityPattern


T = TypeVar("T", bound="VehicleJourney")


@_attrs_define
class VehicleJourney:
    name: str
    """ Name of the object """
    disruptions: list[LinkSchema]
    id: str
    """ Identifier of the object """
    comment: str | Unset = UNSET
    codes: list[Code] | Unset = UNSET
    journey_pattern: JourneyPattern | Unset = UNSET
    calendars: list[Calendar] | Unset = UNSET
    stop_times: list[StopTime] | Unset = UNSET
    comments: list[Comment] | Unset = UNSET
    validity_pattern: ValidityPattern | Unset = UNSET
    trip: Trip | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        disruptions = []
        for disruptions_item_data in self.disruptions:
            disruptions_item = disruptions_item_data.to_dict()
            disruptions.append(disruptions_item)

        id = self.id

        comment = self.comment

        codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.codes, Unset):
            codes = []
            for codes_item_data in self.codes:
                codes_item = codes_item_data.to_dict()
                codes.append(codes_item)

        journey_pattern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.journey_pattern, Unset):
            journey_pattern = self.journey_pattern.to_dict()

        calendars: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.calendars, Unset):
            calendars = []
            for calendars_item_data in self.calendars:
                calendars_item = calendars_item_data.to_dict()
                calendars.append(calendars_item)

        stop_times: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_times, Unset):
            stop_times = []
            for stop_times_item_data in self.stop_times:
                stop_times_item = stop_times_item_data.to_dict()
                stop_times.append(stop_times_item)

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        validity_pattern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validity_pattern, Unset):
            validity_pattern = self.validity_pattern.to_dict()

        trip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trip, Unset):
            trip = self.trip.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "disruptions": disruptions,
                "id": id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if codes is not UNSET:
            field_dict["codes"] = codes
        if journey_pattern is not UNSET:
            field_dict["journey_pattern"] = journey_pattern
        if calendars is not UNSET:
            field_dict["calendars"] = calendars
        if stop_times is not UNSET:
            field_dict["stop_times"] = stop_times
        if comments is not UNSET:
            field_dict["comments"] = comments
        if validity_pattern is not UNSET:
            field_dict["validity_pattern"] = validity_pattern
        if trip is not UNSET:
            field_dict["trip"] = trip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar import Calendar
        from ..models.code import Code
        from ..models.comment import Comment
        from ..models.journey_pattern import JourneyPattern
        from ..models.link_schema import LinkSchema
        from ..models.stop_time import StopTime
        from ..models.trip import Trip
        from ..models.validity_pattern import ValidityPattern

        d = dict(src_dict)
        name = d.pop("name")

        disruptions = []
        _disruptions = d.pop("disruptions")
        for disruptions_item_data in _disruptions:
            disruptions_item = LinkSchema.from_dict(disruptions_item_data)

            disruptions.append(disruptions_item)

        id = d.pop("id")

        comment = d.pop("comment", UNSET)

        _codes = d.pop("codes", UNSET)
        codes: list[Code] | Unset = UNSET
        if _codes is not UNSET:
            codes = []
            for codes_item_data in _codes:
                codes_item = Code.from_dict(codes_item_data)

                codes.append(codes_item)

        _journey_pattern = d.pop("journey_pattern", UNSET)
        journey_pattern: JourneyPattern | Unset
        if isinstance(_journey_pattern, Unset):
            journey_pattern = UNSET
        else:
            journey_pattern = JourneyPattern.from_dict(_journey_pattern)

        _calendars = d.pop("calendars", UNSET)
        calendars: list[Calendar] | Unset = UNSET
        if _calendars is not UNSET:
            calendars = []
            for calendars_item_data in _calendars:
                calendars_item = Calendar.from_dict(calendars_item_data)

                calendars.append(calendars_item)

        _stop_times = d.pop("stop_times", UNSET)
        stop_times: list[StopTime] | Unset = UNSET
        if _stop_times is not UNSET:
            stop_times = []
            for stop_times_item_data in _stop_times:
                stop_times_item = StopTime.from_dict(stop_times_item_data)

                stop_times.append(stop_times_item)

        _comments = d.pop("comments", UNSET)
        comments: list[Comment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = Comment.from_dict(comments_item_data)

                comments.append(comments_item)

        _validity_pattern = d.pop("validity_pattern", UNSET)
        validity_pattern: ValidityPattern | Unset
        if isinstance(_validity_pattern, Unset):
            validity_pattern = UNSET
        else:
            validity_pattern = ValidityPattern.from_dict(_validity_pattern)

        _trip = d.pop("trip", UNSET)
        trip: Trip | Unset
        if isinstance(_trip, Unset):
            trip = UNSET
        else:
            trip = Trip.from_dict(_trip)

        vehicle_journey = cls(
            name=name,
            disruptions=disruptions,
            id=id,
            comment=comment,
            codes=codes,
            journey_pattern=journey_pattern,
            calendars=calendars,
            stop_times=stop_times,
            comments=comments,
            validity_pattern=validity_pattern,
            trip=trip,
        )

        vehicle_journey.additional_properties = d
        return vehicle_journey

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
