from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSchema")


@_attrs_define
class LinkSchema:
    category: str | Unset = UNSET
    title: str | Unset = UNSET
    internal: bool | Unset = UNSET
    value: str | Unset = UNSET
    href: str | Unset = UNSET
    rel: str | Unset = UNSET
    templated: bool | Unset = UNSET
    type_: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        title = self.title

        internal = self.internal

        value = self.value

        href = self.href

        rel = self.rel

        templated = self.templated

        type_ = self.type_

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if title is not UNSET:
            field_dict["title"] = title
        if internal is not UNSET:
            field_dict["internal"] = internal
        if value is not UNSET:
            field_dict["value"] = value
        if href is not UNSET:
            field_dict["href"] = href
        if rel is not UNSET:
            field_dict["rel"] = rel
        if templated is not UNSET:
            field_dict["templated"] = templated
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        title = d.pop("title", UNSET)

        internal = d.pop("internal", UNSET)

        value = d.pop("value", UNSET)

        href = d.pop("href", UNSET)

        rel = d.pop("rel", UNSET)

        templated = d.pop("templated", UNSET)

        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        link_schema = cls(
            category=category,
            title=title,
            internal=internal,
            value=value,
            href=href,
            rel=rel,
            templated=templated,
            type_=type_,
            id=id,
        )

        link_schema.additional_properties = d
        return link_schema

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
