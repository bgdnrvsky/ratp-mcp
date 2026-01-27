from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost import Cost
    from ..models.link_schema import LinkSchema


T = TypeVar("T", bound="Ticket")


@_attrs_define
class Ticket:
    """
    Attributes:
        name (str): Name of the object
        cost (Cost):
        id (str): Identifier of the object
        comment (str | Unset):
        links (list[LinkSchema] | Unset):
        found (bool | Unset):
    """

    name: str
    cost: Cost
    id: str
    comment: str | Unset = UNSET
    links: list[LinkSchema] | Unset = UNSET
    found: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cost = self.cost.to_dict()

        id = self.id

        comment = self.comment

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        found = self.found

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "cost": cost,
                "id": id,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if links is not UNSET:
            field_dict["links"] = links
        if found is not UNSET:
            field_dict["found"] = found

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost import Cost
        from ..models.link_schema import LinkSchema

        d = dict(src_dict)
        name = d.pop("name")

        cost = Cost.from_dict(d.pop("cost"))

        id = d.pop("id")

        comment = d.pop("comment", UNSET)

        _links = d.pop("links", UNSET)
        links: list[LinkSchema] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = LinkSchema.from_dict(links_item_data)

                links.append(links_item)

        found = d.pop("found", UNSET)

        ticket = cls(
            name=name,
            cost=cost,
            id=id,
            comment=comment,
            links=links,
            found=found,
        )

        ticket.additional_properties = d
        return ticket

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
