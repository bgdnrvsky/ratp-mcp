from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graphical_isrochone_geojson import GraphicalIsrochoneGeojson
    from ..models.place import Place


T = TypeVar("T", bound="GraphicalIsrochone")


@_attrs_define
class GraphicalIsrochone:
    """
    Attributes:
        max_duration (int | Unset):
        from_ (Place | Unset):
        geojson (GraphicalIsrochoneGeojson | Unset):
        min_duration (int | Unset):
        min_date_time (str | Unset):
        to (Place | Unset):
        requested_date_time (str | Unset):
        max_date_time (str | Unset):
    """

    max_duration: int | Unset = UNSET
    from_: Place | Unset = UNSET
    geojson: GraphicalIsrochoneGeojson | Unset = UNSET
    min_duration: int | Unset = UNSET
    min_date_time: str | Unset = UNSET
    to: Place | Unset = UNSET
    requested_date_time: str | Unset = UNSET
    max_date_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_duration = self.max_duration

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        geojson: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geojson, Unset):
            geojson = self.geojson.to_dict()

        min_duration = self.min_duration

        min_date_time = self.min_date_time

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        requested_date_time = self.requested_date_time

        max_date_time = self.max_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_duration is not UNSET:
            field_dict["max_duration"] = max_duration
        if from_ is not UNSET:
            field_dict["from"] = from_
        if geojson is not UNSET:
            field_dict["geojson"] = geojson
        if min_duration is not UNSET:
            field_dict["min_duration"] = min_duration
        if min_date_time is not UNSET:
            field_dict["min_date_time"] = min_date_time
        if to is not UNSET:
            field_dict["to"] = to
        if requested_date_time is not UNSET:
            field_dict["requested_date_time"] = requested_date_time
        if max_date_time is not UNSET:
            field_dict["max_date_time"] = max_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graphical_isrochone_geojson import GraphicalIsrochoneGeojson
        from ..models.place import Place

        d = dict(src_dict)
        max_duration = d.pop("max_duration", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Place | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Place.from_dict(_from_)

        _geojson = d.pop("geojson", UNSET)
        geojson: GraphicalIsrochoneGeojson | Unset
        if isinstance(_geojson, Unset):
            geojson = UNSET
        else:
            geojson = GraphicalIsrochoneGeojson.from_dict(_geojson)

        min_duration = d.pop("min_duration", UNSET)

        min_date_time = d.pop("min_date_time", UNSET)

        _to = d.pop("to", UNSET)
        to: Place | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Place.from_dict(_to)

        requested_date_time = d.pop("requested_date_time", UNSET)

        max_date_time = d.pop("max_date_time", UNSET)

        graphical_isrochone = cls(
            max_duration=max_duration,
            from_=from_,
            geojson=geojson,
            min_duration=min_duration,
            min_date_time=min_date_time,
            to=to,
            requested_date_time=requested_date_time,
            max_date_time=max_date_time,
        )

        graphical_isrochone.additional_properties = d
        return graphical_isrochone

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
