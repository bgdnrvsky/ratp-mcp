from enum import Enum


class ImpactedStopStopTimeEffect(str, Enum):
    ADDED = "added"
    DELAYED = "delayed"
    DELETED = "deleted"
    UNCHANGED = "unchanged"

    def __str__(self) -> str:
        return str(self.value)
