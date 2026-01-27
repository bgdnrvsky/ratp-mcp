from enum import Enum


class ChannelTypesItem(str, Enum):
    BEACON = "beacon"
    EMAIL = "email"
    FACEBOOK = "facebook"
    MOBILE = "mobile"
    NOTIFICATION = "notification"
    SMS = "sms"
    TITLE = "title"
    TWITTER = "twitter"
    UNKNOWN_TYPE = "unknown_type"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
