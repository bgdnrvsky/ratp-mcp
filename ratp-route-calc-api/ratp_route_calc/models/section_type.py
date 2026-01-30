from enum import Enum


class SectionType(str, Enum):
    ALIGHTING = "alighting"
    BOARDING = "boarding"
    BSS_PUT_BACK = "bss_put_back"
    BSS_RENT = "bss_rent"
    CROW_FLY = "crow_fly"
    LANDING = "landing"
    LEAVE_PARKING = "leave_parking"
    ON_DEMAND_TRANSPORT = "on_demand_transport"
    PARK = "park"
    PUBLIC_TRANSPORT = "public_transport"
    RIDESHARING = "ridesharing"
    STREET_NETWORK = "street_network"
    TRANSFER = "transfer"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
