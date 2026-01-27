from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.line import Line


T = TypeVar("T", bound="LineGroup")


@_attrs_define
class LineGroup:
    """
    Attributes:
        name (str): Name of the object
        comments (list[Comment]):
        id (str): Identifier of the object
        lines (list[Line] | Unset):
        main_line (Line | Unset):
    """

    name: str
    comments: list[Comment]
    id: str
    lines: list[Line] | Unset = UNSET
    main_line: Line | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        id = self.id

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        main_line: dict[str, Any] | Unset = UNSET
        if not isinstance(self.main_line, Unset):
            main_line = self.main_line.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "comments": comments,
                "id": id,
            }
        )
        if lines is not UNSET:
            field_dict["lines"] = lines
        if main_line is not UNSET:
            field_dict["main_line"] = main_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.line import Line

        d = dict(src_dict)
        name = d.pop("name")

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        id = d.pop("id")

        _lines = d.pop("lines", UNSET)
        lines: list[Line] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = Line.from_dict(lines_item_data)

                lines.append(lines_item)

        _main_line = d.pop("main_line", UNSET)
        main_line: Line | Unset
        if isinstance(_main_line, Unset):
            main_line = UNSET
        else:
            main_line = Line.from_dict(_main_line)

        line_group = cls(
            name=name,
            comments=comments,
            id=id,
            lines=lines,
            main_line=main_line,
        )

        line_group.additional_properties = d
        return line_group

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
