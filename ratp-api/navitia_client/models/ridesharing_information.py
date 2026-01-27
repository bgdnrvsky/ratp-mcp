from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_information import IndividualInformation
    from ..models.seats_description import SeatsDescription


T = TypeVar("T", bound="RidesharingInformation")


@_attrs_define
class RidesharingInformation:
    """
    Attributes:
        operator (str):
        network (str):
        driver (IndividualInformation | Unset):
        seats (SeatsDescription | Unset):
    """

    operator: str
    network: str
    driver: IndividualInformation | Unset = UNSET
    seats: SeatsDescription | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        network = self.network

        driver: dict[str, Any] | Unset = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.to_dict()

        seats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seats, Unset):
            seats = self.seats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
                "network": network,
            }
        )
        if driver is not UNSET:
            field_dict["driver"] = driver
        if seats is not UNSET:
            field_dict["seats"] = seats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.individual_information import IndividualInformation
        from ..models.seats_description import SeatsDescription

        d = dict(src_dict)
        operator = d.pop("operator")

        network = d.pop("network")

        _driver = d.pop("driver", UNSET)
        driver: IndividualInformation | Unset
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = IndividualInformation.from_dict(_driver)

        _seats = d.pop("seats", UNSET)
        seats: SeatsDescription | Unset
        if isinstance(_seats, Unset):
            seats = UNSET
        else:
            seats = SeatsDescription.from_dict(_seats)

        ridesharing_information = cls(
            operator=operator,
            network=network,
            driver=driver,
            seats=seats,
        )

        ridesharing_information.additional_properties = d
        return ridesharing_information

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
