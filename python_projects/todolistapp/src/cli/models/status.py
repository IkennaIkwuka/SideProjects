from enum import Enum, auto


class TaskStatus(Enum):
    EMPTY = auto()
    QUIT = auto()
    INVALID = auto()
    OUT_OF_RANGE = auto()
    EXISTS = auto()
    DELETE_ALL = auto()
    VIEW = auto()


if __name__ == "__main__":
    ...
