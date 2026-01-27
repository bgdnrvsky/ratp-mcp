from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        start_page (int):
        items_on_page (int):
        items_per_page (int):
        total_result (int):
    """

    start_page: int
    items_on_page: int
    items_per_page: int
    total_result: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_page = self.start_page

        items_on_page = self.items_on_page

        items_per_page = self.items_per_page

        total_result = self.total_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_page": start_page,
                "items_on_page": items_on_page,
                "items_per_page": items_per_page,
                "total_result": total_result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_page = d.pop("start_page")

        items_on_page = d.pop("items_on_page")

        items_per_page = d.pop("items_per_page")

        total_result = d.pop("total_result")

        pagination = cls(
            start_page=start_page,
            items_on_page=items_on_page,
            items_per_page=items_per_page,
            total_result=total_result,
        )

        pagination.additional_properties = d
        return pagination

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
