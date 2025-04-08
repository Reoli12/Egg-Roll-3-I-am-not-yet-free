from dataclasses import dataclass
from enum import Enum, auto

type Grid = tuple[tuple[Tile, ...], ...]

class Arrow(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class Order(Enum):
    FRONT = auto()
    BACK = auto()
    LEFT = auto()
    RIGHT = auto()

@dataclass
class Point:
    x: int
    y: int

class Tile(Enum):
    GRASS = auto()
    EGG = auto()
    BRICK = auto()
    PAN = auto()
    NEST = auto()
