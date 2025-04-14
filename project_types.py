from dataclasses import dataclass
from enum import Enum, auto
from tile import Tile, tile_classes
# from type_aliases import Grid


Grid = tuple[tuple[Tile, ...], ...]

class Arrow(Enum):
    UP = '↑'
    DOWN = '↓'
    LEFT = '←'
    RIGHT = '→'

class Feedback(Enum):
    VALID = auto()
    INVALID = auto()

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

class GridParser:
    def parse_grid(self, str_grid: tuple[str, ...]) -> Grid:
        tile_display_to_class = {tile.display: tile for tile in tile_classes}

        res: list[list[Tile]] = []
        for i in range(len(str_grid)):
            current_row: list[Tile] = []
            for j in range(len(str_grid[i])):
                char = str_grid[i][j]
                current_point = Point(i, j)
                tile_subtype = tile_display_to_class[char]
                current_row.append(tile_subtype(current_point))
            res.append(current_row)

        return tuple(tuple(row) for row in res)




