from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context import Context
    from ..models.feed_publisher import FeedPublisher
    from ..models.line import Line
    from ..models.link import Link
    from ..models.pagination import Pagination


T = TypeVar("T", bound="LinesResponse")


@_attrs_define
class LinesResponse:
    pagination: Pagination | Unset = UNSET
    feed_publishers: list[FeedPublisher] | Unset = UNSET
    context: Context | Unset = UNSET
    lines: list[Line] | Unset = UNSET
    links: list[Link] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        feed_publishers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feed_publishers, Unset):
            feed_publishers = []
            for feed_publishers_item_data in self.feed_publishers:
                feed_publishers_item = feed_publishers_item_data.to_dict()
                feed_publishers.append(feed_publishers_item)

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

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
        if feed_publishers is not UNSET:
            field_dict["feed_publishers"] = feed_publishers
        if context is not UNSET:
            field_dict["context"] = context
        if lines is not UNSET:
            field_dict["lines"] = lines
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context import Context
        from ..models.feed_publisher import FeedPublisher
        from ..models.line import Line
        from ..models.link import Link
        from ..models.pagination import Pagination

        d = dict(src_dict)
        _pagination = d.pop("pagination", UNSET)
        pagination: Pagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        _feed_publishers = d.pop("feed_publishers", UNSET)
        feed_publishers: list[FeedPublisher] | Unset = UNSET
        if _feed_publishers is not UNSET:
            feed_publishers = []
            for feed_publishers_item_data in _feed_publishers:
                feed_publishers_item = FeedPublisher.from_dict(feed_publishers_item_data)

                feed_publishers.append(feed_publishers_item)

        _context = d.pop("context", UNSET)
        context: Context | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = Context.from_dict(_context)

        _lines = d.pop("lines", UNSET)
        lines: list[Line] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = Line.from_dict(lines_item_data)

                lines.append(lines_item)

        _links = d.pop("links", UNSET)
        links: list[Link] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = Link.from_dict(links_item_data)

                links.append(links_item)

        lines_response = cls(
            pagination=pagination,
            feed_publishers=feed_publishers,
            context=context,
            lines=lines,
            links=links,
        )

        lines_response.additional_properties = d
        return lines_response

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
