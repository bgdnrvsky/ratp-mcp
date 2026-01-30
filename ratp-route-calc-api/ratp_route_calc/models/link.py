from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    href: str | Unset = UNSET
    templated: bool | Unset = UNSET
    rel: str | Unset = UNSET
    type_: str | Unset = UNSET
    id: str | Unset = UNSET
    internal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        templated = self.templated

        rel = self.rel

        type_ = self.type_

        id = self.id

        internal = self.internal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if templated is not UNSET:
            field_dict["templated"] = templated
        if rel is not UNSET:
            field_dict["rel"] = rel
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if internal is not UNSET:
            field_dict["internal"] = internal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        templated = d.pop("templated", UNSET)

        rel = d.pop("rel", UNSET)

        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        internal = d.pop("internal", UNSET)

        link = cls(
            href=href,
            templated=templated,
            rel=rel,
            type_=type_,
            id=id,
            internal=internal,
        )

        link.additional_properties = d
        return link

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
