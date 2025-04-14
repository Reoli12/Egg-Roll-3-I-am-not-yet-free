import sys
import os

from type_aliases import Grid
from project_types import Arrow

class EggRollView:
    def print_grid(self, grid: Grid):
        for row in grid:
            print(*(tile.display for tile in row), sep = '')

    def print_remaining_moves(self, n: int):
        print(f'moves left: {n} ')

    def print_previous_moves(self, prev_moves: list[Arrow]):
        print('previous moves:', *prev_moves, sep = ' ')

    def print_points(self, n: int):
        print(n)

    def take_user_input(self):
        return input('next move/s: ').strip().lower()
    
    def clear_screen(self):
        if sys.stdout.isatty():
            clear_cmd = 'cls' if os.name == 'nt' else 'clear'
            os.system(clear_cmd)



