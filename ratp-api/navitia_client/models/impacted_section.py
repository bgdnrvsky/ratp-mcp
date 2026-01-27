from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pt_object import PtObject
    from ..models.route import Route


T = TypeVar("T", bound="ImpactedSection")


@_attrs_define
class ImpactedSection:
    """
    Attributes:
        routes (list[Route] | Unset):
        to (PtObject | Unset):
        from_ (PtObject | Unset):
    """

    routes: list[Route] | Unset = UNSET
    to: PtObject | Unset = UNSET
    from_: PtObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routes is not UNSET:
            field_dict["routes"] = routes
        if to is not UNSET:
            field_dict["to"] = to
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pt_object import PtObject
        from ..models.route import Route

        d = dict(src_dict)
        _routes = d.pop("routes", UNSET)
        routes: list[Route] | Unset = UNSET
        if _routes is not UNSET:
            routes = []
            for routes_item_data in _routes:
                routes_item = Route.from_dict(routes_item_data)

                routes.append(routes_item)

        _to = d.pop("to", UNSET)
        to: PtObject | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = PtObject.from_dict(_to)

        _from_ = d.pop("from", UNSET)
        from_: PtObject | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = PtObject.from_dict(_from_)

        impacted_section = cls(
            routes=routes,
            to=to,
            from_=from_,
        )

        impacted_section.additional_properties = d
        return impacted_section

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
