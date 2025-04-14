from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from type_aliases import Grid
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

class RunningStatus(Enum):
    ONGOING = auto()
    DONE = auto()

@dataclass
class Point:
    i: int
    j: int

@dataclass
class DisplayContent:
    current_grid: Grid
    previous_moves: list[Arrow]
    moves_left: int
    points: int




