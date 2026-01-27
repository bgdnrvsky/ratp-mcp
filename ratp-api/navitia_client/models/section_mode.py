from enum import Enum


class SectionMode(str, Enum):
    BIKE = "bike"
    BSS = "bss"
    CAR = "car"
    CARNOPARK = "carnopark"
    RIDESHARING = "ridesharing"
    TAXI = "taxi"
    WALKING = "walking"

    def __str__(self) -> str:
        return str(self.value)
