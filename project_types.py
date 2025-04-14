from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
# from tile import Tile


class Arrow(Enum):
    UP = '↑'
    DOWN = '↓'
    LEFT = '←'
    RIGHT = '→'

class Order(Enum):
    FRONT = Arrow.UP
    BACK = Arrow.DOWN
    LEFT = Arrow.LEFT
    RIGHT = Arrow.RIGHT

@dataclass
class Point:
    i: int
    j: int



