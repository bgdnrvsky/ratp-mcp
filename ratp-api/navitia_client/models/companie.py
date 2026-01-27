from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.code import Code


T = TypeVar("T", bound="Companie")


@_attrs_define
class Companie:
    """
    Attributes:
        codes (list[Code]):
        id (str): Identifier of the object
        name (str): Name of the object
    """

    codes: list[Code]
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codes = []
        for codes_item_data in self.codes:
            codes_item = codes_item_data.to_dict()
            codes.append(codes_item)

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "codes": codes,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code import Code

        d = dict(src_dict)
        codes = []
        _codes = d.pop("codes")
        for codes_item_data in _codes:
            codes_item = Code.from_dict(codes_item_data)

            codes.append(codes_item)

        id = d.pop("id")

        name = d.pop("name")

        companie = cls(
            codes=codes,
            id=id,
            name=name,
        )

        companie.additional_properties = d
        return companie

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
