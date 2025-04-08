from enum import Enum, auto

class Tile(Enum):
    GRASS = auto()
    EGG = auto()
    BRICK = auto()
    PAN = auto()
    NEST = auto()

class Arrow(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()