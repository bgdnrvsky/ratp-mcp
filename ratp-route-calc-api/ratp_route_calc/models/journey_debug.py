from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JourneyDebug")


@_attrs_define
class JourneyDebug:
    nb_vj_extentions: int
    """ Number of stay-in """
    nb_sections: int
    """ Number of sections """
    streetnetwork_duration: int
    """ Total duration of streetnetwork use (seconds) """
    transfer_duration: int
    """ Total duration of transfers (seconds) """
    min_waiting_duration: int
    """ Minimum on all waiting durations (seconds) """
    internal_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nb_vj_extentions = self.nb_vj_extentions

        nb_sections = self.nb_sections

        streetnetwork_duration = self.streetnetwork_duration

        transfer_duration = self.transfer_duration

        min_waiting_duration = self.min_waiting_duration

        internal_id = self.internal_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nb_vj_extentions": nb_vj_extentions,
                "nb_sections": nb_sections,
                "streetnetwork_duration": streetnetwork_duration,
                "transfer_duration": transfer_duration,
                "min_waiting_duration": min_waiting_duration,
            }
        )
        if internal_id is not UNSET:
            field_dict["internal_id"] = internal_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nb_vj_extentions = d.pop("nb_vj_extentions")

        nb_sections = d.pop("nb_sections")

        streetnetwork_duration = d.pop("streetnetwork_duration")

        transfer_duration = d.pop("transfer_duration")

        min_waiting_duration = d.pop("min_waiting_duration")

        internal_id = d.pop("internal_id", UNSET)

        journey_debug = cls(
            nb_vj_extentions=nb_vj_extentions,
            nb_sections=nb_sections,
            streetnetwork_duration=streetnetwork_duration,
            transfer_duration=transfer_duration,
            min_waiting_duration=min_waiting_duration,
            internal_id=internal_id,
        )

        journey_debug.additional_properties = d
        return journey_debug

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
