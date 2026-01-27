from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amount import Amount


T = TypeVar("T", bound="CO2")


@_attrs_define
class CO2:
    """
    Attributes:
        co2_emission (Amount | Unset):
    """

    co2_emission: Amount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co2_emission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.co2_emission, Unset):
            co2_emission = self.co2_emission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co2_emission is not UNSET:
            field_dict["co2_emission"] = co2_emission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amount import Amount

        d = dict(src_dict)
        _co2_emission = d.pop("co2_emission", UNSET)
        co2_emission: Amount | Unset
        if isinstance(_co2_emission, Unset):
            co2_emission = UNSET
        else:
            co2_emission = Amount.from_dict(_co2_emission)

        co2 = cls(
            co2_emission=co2_emission,
        )

        co2.additional_properties = d
        return co2

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
