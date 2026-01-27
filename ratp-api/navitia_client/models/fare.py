from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost import Cost
    from ..models.link_schema import LinkSchema


T = TypeVar("T", bound="Fare")


@_attrs_define
class Fare:
    """
    Attributes:
        links (list[LinkSchema]):
        found (bool | Unset):
        total (Cost | Unset):
    """

    links: list[LinkSchema]
    found: bool | Unset = UNSET
    total: Cost | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        found = self.found

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
            }
        )
        if found is not UNSET:
            field_dict["found"] = found
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost import Cost
        from ..models.link_schema import LinkSchema

        d = dict(src_dict)
        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        found = d.pop("found", UNSET)

        _total = d.pop("total", UNSET)
        total: Cost | Unset
        if isinstance(_total, Unset):
            total = UNSET
        else:
            total = Cost.from_dict(_total)

        fare = cls(
            links=links,
            found=found,
            total=total,
        )

        fare.additional_properties = d
        return fare

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
