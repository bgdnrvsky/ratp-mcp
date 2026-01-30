from enum import Enum


class SectionAdditionalInformationsItem(str, Enum):
    HAS_DATETIME_ESTIMATED = "has_datetime_estimated"
    ODT_WITH_STOP_POINT = "odt_with_stop_point"
    ODT_WITH_STOP_TIME = "odt_with_stop_time"
    ODT_WITH_ZONE = "odt_with_zone"
    REGULAR = "regular"
    STAY_IN = "stay_in"

    def __str__(self) -> str:
        return str(self.value)
