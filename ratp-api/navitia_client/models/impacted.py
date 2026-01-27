from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impacted_section import ImpactedSection
    from ..models.impacted_stop import ImpactedStop
    from ..models.pt_object import PtObject


T = TypeVar("T", bound="Impacted")


@_attrs_define
class Impacted:
    """
    Attributes:
        impacted_stops (list[ImpactedStop] | Unset):
        pt_object (PtObject | Unset):
        impacted_section (ImpactedSection | Unset):
    """

    impacted_stops: list[ImpactedStop] | Unset = UNSET
    pt_object: PtObject | Unset = UNSET
    impacted_section: ImpactedSection | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impacted_stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.impacted_stops, Unset):
            impacted_stops = []
            for impacted_stops_item_data in self.impacted_stops:
                impacted_stops_item = impacted_stops_item_data.to_dict()
                impacted_stops.append(impacted_stops_item)

        pt_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pt_object, Unset):
            pt_object = self.pt_object.to_dict()

        impacted_section: dict[str, Any] | Unset = UNSET
        if not isinstance(self.impacted_section, Unset):
            impacted_section = self.impacted_section.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if impacted_stops is not UNSET:
            field_dict["impacted_stops"] = impacted_stops
        if pt_object is not UNSET:
            field_dict["pt_object"] = pt_object
        if impacted_section is not UNSET:
            field_dict["impacted_section"] = impacted_section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impacted_section import ImpactedSection
        from ..models.impacted_stop import ImpactedStop
        from ..models.pt_object import PtObject

        d = dict(src_dict)
        _impacted_stops = d.pop("impacted_stops", UNSET)
        impacted_stops: list[ImpactedStop] | Unset = UNSET
        if _impacted_stops is not UNSET:
            impacted_stops = []
            for impacted_stops_item_data in _impacted_stops:
                impacted_stops_item = ImpactedStop.from_dict(impacted_stops_item_data)

                impacted_stops.append(impacted_stops_item)

        _pt_object = d.pop("pt_object", UNSET)
        pt_object: PtObject | Unset
        if isinstance(_pt_object, Unset):
            pt_object = UNSET
        else:
            pt_object = PtObject.from_dict(_pt_object)

        _impacted_section = d.pop("impacted_section", UNSET)
        impacted_section: ImpactedSection | Unset
        if isinstance(_impacted_section, Unset):
            impacted_section = UNSET
        else:
            impacted_section = ImpactedSection.from_dict(_impacted_section)

        impacted = cls(
            impacted_stops=impacted_stops,
            pt_object=pt_object,
            impacted_section=impacted_section,
        )

        impacted.additional_properties = d
        return impacted

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
