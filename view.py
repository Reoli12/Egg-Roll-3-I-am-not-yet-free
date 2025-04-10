from type_aliases import Grid

class EggRollView:
    def print_grid(self, grid: Grid):
        for row in grid:
            print(*(tile.display for tile in row), sep = '')