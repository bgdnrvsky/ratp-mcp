from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_schema import LinkSchema


T = TypeVar("T", bound="DateTimeType")


@_attrs_define
class DateTimeType:
    """
    Attributes:
        date_time (str):
        additional_informations (list[str]):
        data_freshness (str):
        links (list[LinkSchema]):
        base_date_time (str | Unset):
    """

    date_time: str
    additional_informations: list[str]
    data_freshness: str
    links: list[LinkSchema]
    base_date_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_time = self.date_time

        additional_informations = self.additional_informations

        data_freshness = self.data_freshness

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()
            links.append(links_item)

        base_date_time = self.base_date_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date_time": date_time,
                "additional_informations": additional_informations,
                "data_freshness": data_freshness,
                "links": links,
            }
        )
        if base_date_time is not UNSET:
            field_dict["base_date_time"] = base_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_schema import LinkSchema

        d = dict(src_dict)
        date_time = d.pop("date_time")

        additional_informations = cast(list[str], d.pop("additional_informations"))

        data_freshness = d.pop("data_freshness")

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = LinkSchema.from_dict(links_item_data)

            links.append(links_item)

        base_date_time = d.pop("base_date_time", UNSET)

        date_time_type = cls(
            date_time=date_time,
            additional_informations=additional_informations,
            data_freshness=data_freshness,
            links=links,
            base_date_time=base_date_time,
        )

        date_time_type.additional_properties = d
        return date_time_type

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
