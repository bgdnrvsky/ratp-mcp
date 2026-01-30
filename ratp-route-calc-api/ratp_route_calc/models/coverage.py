from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coverage_error import CoverageError


T = TypeVar("T", bound="Coverage")


@_attrs_define
class Coverage:
    name: str
    """ Name of the coverage """
    shape: str
    """ GeoJSON of the shape of the coverage """
    id: str
    """ Identifier of the coverage """
    status: str | Unset = UNSET
    dataset_created_at: str | Unset = UNSET
    """ Creation date of the dataset """
    start_production_date: str | Unset = UNSET
    """ Beginning of the production period. We only have data on this production period """
    end_production_date: str | Unset = UNSET
    """ End of the production period. We only have data on this production period """
    error: CoverageError | Unset = UNSET
    last_load_at: str | Unset = UNSET
    """ Datetime of the last data loading """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        shape = self.shape

        id = self.id

        status = self.status

        dataset_created_at = self.dataset_created_at

        start_production_date = self.start_production_date

        end_production_date = self.end_production_date

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        last_load_at = self.last_load_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "shape": shape,
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if dataset_created_at is not UNSET:
            field_dict["dataset_created_at"] = dataset_created_at
        if start_production_date is not UNSET:
            field_dict["start_production_date"] = start_production_date
        if end_production_date is not UNSET:
            field_dict["end_production_date"] = end_production_date
        if error is not UNSET:
            field_dict["error"] = error
        if last_load_at is not UNSET:
            field_dict["last_load_at"] = last_load_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.coverage_error import CoverageError

        d = dict(src_dict)
        name = d.pop("name")

        shape = d.pop("shape")

        id = d.pop("id")

        status = d.pop("status", UNSET)

        dataset_created_at = d.pop("dataset_created_at", UNSET)

        start_production_date = d.pop("start_production_date", UNSET)

        end_production_date = d.pop("end_production_date", UNSET)

        _error = d.pop("error", UNSET)
        error: CoverageError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = CoverageError.from_dict(_error)

        last_load_at = d.pop("last_load_at", UNSET)

        coverage = cls(
            name=name,
            shape=shape,
            id=id,
            status=status,
            dataset_created_at=dataset_created_at,
            start_production_date=start_production_date,
            end_production_date=end_production_date,
            error=error,
            last_load_at=last_load_at,
        )

        coverage.additional_properties = d
        return coverage

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
