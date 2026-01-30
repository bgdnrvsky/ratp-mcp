from enum import Enum


class SectionTransferType(str, Enum):
    STAY_IN = "stay_in"
    WALKING = "walking"

    def __str__(self) -> str:
        return str(self.value)
