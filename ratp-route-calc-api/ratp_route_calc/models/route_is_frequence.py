from enum import Enum


class RouteIsFrequence(str, Enum):
    FALSE = "False"

    def __str__(self) -> str:
        return str(self.value)
