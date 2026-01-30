from enum import Enum


class PtObjectEmbeddedType(str, Enum):
    ADDRESS = "address"
    ADMINISTRATIVE_REGION = "administrative_region"
    CALENDAR = "calendar"
    COMMERCIAL_MODE = "commercial_mode"
    COMPANY = "company"
    CONNECTION = "connection"
    CONTRIBUTOR = "contributor"
    DATASET = "dataset"
    IMPACT = "impact"
    JOURNEY_PATTERN = "journey_pattern"
    JOURNEY_PATTERN_POINT = "journey_pattern_point"
    LINE = "line"
    LINE_GROUP = "line_group"
    NETWORK = "network"
    PHYSICAL_MODE = "physical_mode"
    POI = "poi"
    POITYPE = "poitype"
    ROUTE = "route"
    STOP_AREA = "stop_area"
    STOP_POINT = "stop_point"
    TRIP = "trip"
    VEHICLE_JOURNEY = "vehicle_journey"

    def __str__(self) -> str:
        return str(self.value)
