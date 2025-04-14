from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
# from tile import Tile


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
    i: int
    j: int

# class Tile(Enum):
#     GRASS = auto()
#     EGG = auto()
#     BRICK = auto()
#     PAN = auto()
#     NEST = auto()

