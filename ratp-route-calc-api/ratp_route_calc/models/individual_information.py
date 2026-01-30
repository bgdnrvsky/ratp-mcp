from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.individual_information_gender import IndividualInformationGender
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_rating import IndividualRating


T = TypeVar("T", bound="IndividualInformation")


@_attrs_define
class IndividualInformation:
    alias: str
    image: str | Unset = UNSET
    gender: IndividualInformationGender | Unset = UNSET
    rating: IndividualRating | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        image = self.image

        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if gender is not UNSET:
            field_dict["gender"] = gender
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.individual_rating import IndividualRating

        d = dict(src_dict)
        alias = d.pop("alias")

        image = d.pop("image", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: IndividualInformationGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = IndividualInformationGender(_gender)

        _rating = d.pop("rating", UNSET)
        rating: IndividualRating | Unset
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = IndividualRating.from_dict(_rating)

        individual_information = cls(
            alias=alias,
            image=image,
            gender=gender,
            rating=rating,
        )

        individual_information.additional_properties = d
        return individual_information

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
