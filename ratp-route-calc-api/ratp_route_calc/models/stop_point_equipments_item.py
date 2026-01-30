from enum import Enum


class StopPointEquipmentsItem(str, Enum):
    HAS_AIR_CONDITIONED = "has_air_conditioned"
    HAS_APPROPRIATE_ESCORT = "has_appropriate_escort"
    HAS_APPROPRIATE_SIGNAGE = "has_appropriate_signage"
    HAS_AUDIBLE_ANNOUNCEMENT = "has_audible_announcement"
    HAS_BIKE_ACCEPTED = "has_bike_accepted"
    HAS_BIKE_DEPOT = "has_bike_depot"
    HAS_ELEVATOR = "has_elevator"
    HAS_ESCALATOR = "has_escalator"
    HAS_SCHOOL_VEHICLE = "has_school_vehicle"
    HAS_SHELTERED = "has_sheltered"
    HAS_VISUAL_ANNOUNCEMENT = "has_visual_announcement"
    HAS_WHEELCHAIR_ACCESSIBILITY = "has_wheelchair_accessibility"
    HAS_WHEELCHAIR_BOARDING = "has_wheelchair_boarding"

    def __str__(self) -> str:
        return str(self.value)
