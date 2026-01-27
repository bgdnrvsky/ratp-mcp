from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.co2 import CO2


T = TypeVar("T", bound="Context")


@_attrs_define
class Context:
    """
    Attributes:
        timezone (str | Unset): Timezone of any datetime in the response, default value Africa/Abidjan (UTC)
        current_datetime (str | Unset): The datetime of the request (considered as "now")
        car_direct_path (CO2 | Unset):
    """

    timezone: str | Unset = UNSET
    current_datetime: str | Unset = UNSET
    car_direct_path: CO2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timezone = self.timezone

        current_datetime = self.current_datetime

        car_direct_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.car_direct_path, Unset):
            car_direct_path = self.car_direct_path.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if current_datetime is not UNSET:
            field_dict["current_datetime"] = current_datetime
        if car_direct_path is not UNSET:
            field_dict["car_direct_path"] = car_direct_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.co2 import CO2

        d = dict(src_dict)
        timezone = d.pop("timezone", UNSET)

        current_datetime = d.pop("current_datetime", UNSET)

        _car_direct_path = d.pop("car_direct_path", UNSET)
        car_direct_path: CO2 | Unset
        if isinstance(_car_direct_path, Unset):
            car_direct_path = UNSET
        else:
            car_direct_path = CO2.from_dict(_car_direct_path)

        context = cls(
            timezone=timezone,
            current_datetime=current_datetime,
            car_direct_path=car_direct_path,
        )

        context.additional_properties = d
        return context

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
