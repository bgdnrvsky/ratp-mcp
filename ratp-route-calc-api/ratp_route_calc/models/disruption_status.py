from enum import Enum


class DisruptionStatus(str, Enum):
    ACTIVE = "active"
    FUTURE = "future"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
