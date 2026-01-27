from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_effect import SeverityEffect
from ..types import UNSET, Unset

T = TypeVar("T", bound="Severity")


@_attrs_define
class Severity:
    """
    Attributes:
        color (str | Unset):
        priority (int | Unset):
        name (str | Unset):
        effect (SeverityEffect | Unset):
    """

    color: str | Unset = UNSET
    priority: int | Unset = UNSET
    name: str | Unset = UNSET
    effect: SeverityEffect | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color = self.color

        priority = self.priority

        name = self.name

        effect: str | Unset = UNSET
        if not isinstance(self.effect, Unset):
            effect = self.effect.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if priority is not UNSET:
            field_dict["priority"] = priority
        if name is not UNSET:
            field_dict["name"] = name
        if effect is not UNSET:
            field_dict["effect"] = effect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        priority = d.pop("priority", UNSET)

        name = d.pop("name", UNSET)

        _effect = d.pop("effect", UNSET)
        effect: SeverityEffect | Unset
        if isinstance(_effect, Unset):
            effect = UNSET
        else:
            effect = SeverityEffect(_effect)

        severity = cls(
            color=color,
            priority=priority,
            name=name,
            effect=effect,
        )

        severity.additional_properties = d
        return severity

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
