from enum import Enum


class StandsStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
