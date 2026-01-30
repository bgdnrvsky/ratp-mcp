from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context import Context
    from ..models.link import Link
    from ..models.pagination import Pagination
    from ..models.stop_area import StopArea


T = TypeVar("T", bound="StopAreasResponse")


@_attrs_define
class StopAreasResponse:
    pagination: Pagination | Unset = UNSET
    stop_areas: list[StopArea] | Unset = UNSET
    context: Context | Unset = UNSET
    links: list[Link] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        stop_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stop_areas, Unset):
            stop_areas = []
            for stop_areas_item_data in self.stop_areas:
                stop_areas_item = stop_areas_item_data.to_dict()
                stop_areas.append(stop_areas_item)

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if stop_areas is not UNSET:
            field_dict["stop_areas"] = stop_areas
        if context is not UNSET:
            field_dict["context"] = context
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context import Context
        from ..models.link import Link
        from ..models.pagination import Pagination
        from ..models.stop_area import StopArea

        d = dict(src_dict)
        _pagination = d.pop("pagination", UNSET)
        pagination: Pagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        _stop_areas = d.pop("stop_areas", UNSET)
        stop_areas: list[StopArea] | Unset = UNSET
        if _stop_areas is not UNSET:
            stop_areas = []
            for stop_areas_item_data in _stop_areas:
                stop_areas_item = StopArea.from_dict(stop_areas_item_data)

                stop_areas.append(stop_areas_item)

        _context = d.pop("context", UNSET)
        context: Context | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = Context.from_dict(_context)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        stop_areas_response = cls(
            pagination=pagination,
            stop_areas=stop_areas,
            context=context,
            links=links,
        )

        stop_areas_response.additional_properties = d
        return stop_areas_response

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
