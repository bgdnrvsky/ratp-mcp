from enum import Enum


class StopDateTimeAdditionalInformationsItem(str, Enum):
    DATE_TIME_ESTIMATED = "date_time_estimated"
    DROP_OFF_ONLY = "drop_off_only"
    ON_DEMAND_TRANSPORT = "on_demand_transport"
    PICK_UP_ONLY = "pick_up_only"

    def __str__(self) -> str:
        return str(self.value)
