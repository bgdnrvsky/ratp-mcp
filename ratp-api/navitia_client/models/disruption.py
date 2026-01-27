from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.disruption_status import DisruptionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disruption_property import DisruptionProperty
    from ..models.impacted import Impacted
    from ..models.message import Message
    from ..models.period import Period
    from ..models.severity import Severity


T = TypeVar("T", bound="Disruption")


@_attrs_define
class Disruption:
    """
    Attributes:
        id (str):
        contributor (str):
        cause (str):
        status (DisruptionStatus | Unset):
        category (str | Unset):
        severity (Severity | Unset):
        tags (list[str] | Unset):
        messages (list[Message] | Unset):
        application_periods (list[Period] | Unset):
        impact_id (str | Unset):
        disruption_id (str | Unset):
        updated_at (str | Unset):
        uri (str | Unset):
        impacted_objects (list[Impacted] | Unset):
        disruption_uri (str | Unset):
        properties (list[DisruptionProperty] | Unset):
    """

    id: str
    contributor: str
    cause: str
    status: DisruptionStatus | Unset = UNSET
    category: str | Unset = UNSET
    severity: Severity | Unset = UNSET
    tags: list[str] | Unset = UNSET
    messages: list[Message] | Unset = UNSET
    application_periods: list[Period] | Unset = UNSET
    impact_id: str | Unset = UNSET
    disruption_id: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    uri: str | Unset = UNSET
    impacted_objects: list[Impacted] | Unset = UNSET
    disruption_uri: str | Unset = UNSET
    properties: list[DisruptionProperty] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contributor = self.contributor

        cause = self.cause

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        category = self.category

        severity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        application_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.application_periods, Unset):
            application_periods = []
            for application_periods_item_data in self.application_periods:
                application_periods_item = application_periods_item_data.to_dict()
                application_periods.append(application_periods_item)

        impact_id = self.impact_id

        disruption_id = self.disruption_id

        updated_at = self.updated_at

        uri = self.uri

        impacted_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.impacted_objects, Unset):
            impacted_objects = []
            for impacted_objects_item_data in self.impacted_objects:
                impacted_objects_item = impacted_objects_item_data.to_dict()
                impacted_objects.append(impacted_objects_item)

        disruption_uri = self.disruption_uri

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contributor": contributor,
                "cause": cause,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if category is not UNSET:
            field_dict["category"] = category
        if severity is not UNSET:
            field_dict["severity"] = severity
        if tags is not UNSET:
            field_dict["tags"] = tags
        if messages is not UNSET:
            field_dict["messages"] = messages
        if application_periods is not UNSET:
            field_dict["application_periods"] = application_periods
        if impact_id is not UNSET:
            field_dict["impact_id"] = impact_id
        if disruption_id is not UNSET:
            field_dict["disruption_id"] = disruption_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if uri is not UNSET:
            field_dict["uri"] = uri
        if impacted_objects is not UNSET:
            field_dict["impacted_objects"] = impacted_objects
        if disruption_uri is not UNSET:
            field_dict["disruption_uri"] = disruption_uri
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disruption_property import DisruptionProperty
        from ..models.impacted import Impacted
        from ..models.message import Message
        from ..models.period import Period
        from ..models.severity import Severity

        d = dict(src_dict)
        id = d.pop("id")

        contributor = d.pop("contributor")

        cause = d.pop("cause")

        _status = d.pop("status", UNSET)
        status: DisruptionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DisruptionStatus(_status)

        category = d.pop("category", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Severity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = Severity.from_dict(_severity)

        tags = cast(list[str], d.pop("tags", UNSET))

        _messages = d.pop("messages", UNSET)
        messages: list[Message] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = Message.from_dict(messages_item_data)

                messages.append(messages_item)

        _application_periods = d.pop("application_periods", UNSET)
        application_periods: list[Period] | Unset = UNSET
        if _application_periods is not UNSET:
            application_periods = []
            for application_periods_item_data in _application_periods:
                application_periods_item = Period.from_dict(application_periods_item_data)

                application_periods.append(application_periods_item)

        impact_id = d.pop("impact_id", UNSET)

        disruption_id = d.pop("disruption_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        uri = d.pop("uri", UNSET)

        _impacted_objects = d.pop("impacted_objects", UNSET)
        impacted_objects: list[Impacted] | Unset = UNSET
        if _impacted_objects is not UNSET:
            impacted_objects = []
            for impacted_objects_item_data in _impacted_objects:
                impacted_objects_item = Impacted.from_dict(impacted_objects_item_data)

                impacted_objects.append(impacted_objects_item)

        disruption_uri = d.pop("disruption_uri", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[DisruptionProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = DisruptionProperty.from_dict(properties_item_data)

                properties.append(properties_item)

        disruption = cls(
            id=id,
            contributor=contributor,
            cause=cause,
            status=status,
            category=category,
            severity=severity,
            tags=tags,
            messages=messages,
            application_periods=application_periods,
            impact_id=impact_id,
            disruption_id=disruption_id,
            updated_at=updated_at,
            uri=uri,
            impacted_objects=impacted_objects,
            disruption_uri=disruption_uri,
            properties=properties,
        )

        disruption.additional_properties = d
        return disruption

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
