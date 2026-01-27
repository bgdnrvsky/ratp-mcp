from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heat_matrix_schema import HeatMatrixSchema
    from ..models.place import Place


T = TypeVar("T", bound="HeatMap")


@_attrs_define
class HeatMap:
    """
    Attributes:
        to (Place | Unset):
        requested_date_time (str | Unset):
        from_ (Place | Unset):
        heat_matrix (HeatMatrixSchema | Unset):
    """

    to: Place | Unset = UNSET
    requested_date_time: str | Unset = UNSET
    from_: Place | Unset = UNSET
    heat_matrix: HeatMatrixSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        requested_date_time = self.requested_date_time

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        heat_matrix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heat_matrix, Unset):
            heat_matrix = self.heat_matrix.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to is not UNSET:
            field_dict["to"] = to
        if requested_date_time is not UNSET:
            field_dict["requested_date_time"] = requested_date_time
        if from_ is not UNSET:
            field_dict["from"] = from_
        if heat_matrix is not UNSET:
            field_dict["heat_matrix"] = heat_matrix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.heat_matrix_schema import HeatMatrixSchema
        from ..models.place import Place

        d = dict(src_dict)
        _to = d.pop("to", UNSET)
        to: Place | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = Place.from_dict(_to)

        requested_date_time = d.pop("requested_date_time", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: Place | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = Place.from_dict(_from_)

        _heat_matrix = d.pop("heat_matrix", UNSET)
        heat_matrix: HeatMatrixSchema | Unset
        if isinstance(_heat_matrix, Unset):
            heat_matrix = UNSET
        else:
            heat_matrix = HeatMatrixSchema.from_dict(_heat_matrix)

        heat_map = cls(
            to=to,
            requested_date_time=requested_date_time,
            from_=from_,
            heat_matrix=heat_matrix,
        )

        heat_map.additional_properties = d
        return heat_map

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
