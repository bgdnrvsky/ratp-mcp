from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.note_category import NoteCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    id: str
    category: NoteCategory | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _category = d.pop("category", UNSET)
        category: NoteCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = NoteCategory(_category)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        note = cls(
            id=id,
            category=category,
            type_=type_,
            value=value,
        )

        note.additional_properties = d
        return note

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
