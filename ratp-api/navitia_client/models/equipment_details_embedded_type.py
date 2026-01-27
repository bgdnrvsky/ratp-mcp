from enum import Enum


class EquipmentDetailsEmbeddedType(str, Enum):
    ELEVATOR = "elevator"
    ESCALATOR = "escalator"

    def __str__(self) -> str:
        return str(self.value)
