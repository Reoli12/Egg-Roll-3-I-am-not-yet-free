from model import EggRollModel
from view import EggRollView
from tile import Tile, Egg, EmptyNest, Grass, OccupiedNest, Pan, Wall
from type_aliases import Grid
from project_types import Point, Order

tile_classes = (Egg, EmptyNest, Grass, OccupiedNest, Pan, Wall)

tile_display_to_class = {tile.display: tile for tile in tile_classes}

def parse_text_grid(grid: tuple[str, ...]) -> Grid:

    res: list[list[Tile]] = []
    for i in range(len(grid)):
        current_row: list[Tile] = []
        for j in range(len(grid[i])):
            char = grid[i][j]
            current_point = Point(i, j)
            tile_subtype = tile_display_to_class[char]
            current_row.append(tile_subtype(current_point))
        res.append(current_row)
        

    return tuple(tuple(row) for row in res)

test = (
    '🧱🧱🧱🧱🧱🧱🧱🧱',
    '🧱🍳🟩🟩🟩🥚🥚🧱',
    '🧱🟩🟩🟩🟩🥚🥚🧱',
    '🧱🍳🟩🟩🟩🟩🥚🧱',
    '🧱🟩🟩🟩🟩🟩🟩🧱',
    '🧱🟩🟩🟩🟩🪹🪹🧱',
    '🧱🧱🧱🧱🧱🧱🧱🧱',
)

tileTest = parse_text_grid(test)

model = EggRollModel(tileTest, 10)
view = EggRollView()
view.print_grid(tileTest)

a = model.roll([Order.BACK])
view.print_grid(a)


