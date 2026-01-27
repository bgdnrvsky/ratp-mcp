from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.current_availability_status import CurrentAvailabilityStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cause import Cause
    from ..models.effect import Effect
    from ..models.period import Period


T = TypeVar("T", bound="CurrentAvailability")


@_attrs_define
class CurrentAvailability:
    """
    Attributes:
        status (CurrentAvailabilityStatus | Unset):
        effect (Effect | Unset):
        cause (Cause | Unset):
        periods (list[Period] | Unset):
        updated_at (str | Unset):
    """

    status: CurrentAvailabilityStatus | Unset = UNSET
    effect: Effect | Unset = UNSET
    cause: Cause | Unset = UNSET
    periods: list[Period] | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        effect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effect, Unset):
            effect = self.effect.to_dict()

        cause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.to_dict()

        periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if effect is not UNSET:
            field_dict["effect"] = effect
        if cause is not UNSET:
            field_dict["cause"] = cause
        if periods is not UNSET:
            field_dict["periods"] = periods
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cause import Cause
        from ..models.effect import Effect
        from ..models.period import Period

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: CurrentAvailabilityStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CurrentAvailabilityStatus(_status)

        _effect = d.pop("effect", UNSET)
        effect: Effect | Unset
        if isinstance(_effect, Unset):
            effect = UNSET
        else:
            effect = Effect.from_dict(_effect)

        _cause = d.pop("cause", UNSET)
        cause: Cause | Unset
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = Cause.from_dict(_cause)

        _periods = d.pop("periods", UNSET)
        periods: list[Period] | Unset = UNSET
        if _periods is not UNSET:
            periods = []
            for periods_item_data in _periods:
                periods_item = Period.from_dict(periods_item_data)

                periods.append(periods_item)

        updated_at = d.pop("updated_at", UNSET)

        current_availability = cls(
            status=status,
            effect=effect,
            cause=cause,
            periods=periods,
            updated_at=updated_at,
        )

        current_availability.additional_properties = d
        return current_availability

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
