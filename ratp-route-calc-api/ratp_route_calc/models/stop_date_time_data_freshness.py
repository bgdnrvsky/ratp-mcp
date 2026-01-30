from enum import Enum


class StopDateTimeDataFreshness(str, Enum):
    ADAPTED_SCHEDULE = "adapted_schedule"
    BASE_SCHEDULE = "base_schedule"
    REALTIME = "realtime"

    def __str__(self) -> str:
        return str(self.value)
