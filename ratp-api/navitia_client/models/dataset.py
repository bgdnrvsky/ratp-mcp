from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contributor import Contributor


T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """
    Attributes:
        id (str): Identifier of the object
        realtime_level (str | Unset):
        description (str | Unset):
        system (str | Unset): Type of dataset provided (GTFS, Chouette, ...)
        start_validation_date (str | Unset): Start of the validity period for the dataset
        end_validation_date (str | Unset): End of the validity period for the dataset
        contributor (Contributor | Unset):
    """

    id: str
    realtime_level: str | Unset = UNSET
    description: str | Unset = UNSET
    system: str | Unset = UNSET
    start_validation_date: str | Unset = UNSET
    end_validation_date: str | Unset = UNSET
    contributor: Contributor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        realtime_level = self.realtime_level

        description = self.description

        system = self.system

        start_validation_date = self.start_validation_date

        end_validation_date = self.end_validation_date

        contributor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contributor, Unset):
            contributor = self.contributor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if realtime_level is not UNSET:
            field_dict["realtime_level"] = realtime_level
        if description is not UNSET:
            field_dict["description"] = description
        if system is not UNSET:
            field_dict["system"] = system
        if start_validation_date is not UNSET:
            field_dict["start_validation_date"] = start_validation_date
        if end_validation_date is not UNSET:
            field_dict["end_validation_date"] = end_validation_date
        if contributor is not UNSET:
            field_dict["contributor"] = contributor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contributor import Contributor

        d = dict(src_dict)
        id = d.pop("id")

        realtime_level = d.pop("realtime_level", UNSET)

        description = d.pop("description", UNSET)

        system = d.pop("system", UNSET)

        start_validation_date = d.pop("start_validation_date", UNSET)

        end_validation_date = d.pop("end_validation_date", UNSET)

        _contributor = d.pop("contributor", UNSET)
        contributor: Contributor | Unset
        if isinstance(_contributor, Unset):
            contributor = UNSET
        else:
            contributor = Contributor.from_dict(_contributor)

        dataset = cls(
            id=id,
            realtime_level=realtime_level,
            description=description,
            system=system,
            start_validation_date=start_validation_date,
            end_validation_date=end_validation_date,
            contributor=contributor,
        )

        dataset.additional_properties = d
        return dataset

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
