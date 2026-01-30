from enum import Enum


class NoteCategory(str, Enum):
    COMMENT = "comment"
    TERMINUS = "terminus"

    def __str__(self) -> str:
        return str(self.value)
