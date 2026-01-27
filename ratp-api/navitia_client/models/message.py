from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """
    Attributes:
        text (str | Unset):
        channel (Channel | Unset):
    """

    text: str | Unset = UNSET
    channel: Channel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel import Channel

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: Channel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = Channel.from_dict(_channel)

        message = cls(
            text=text,
            channel=channel,
        )

        message.additional_properties = d
        return message

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
