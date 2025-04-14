import sys
import os

from type_aliases import Grid
from project_types import Arrow, DisplayContent

class EggRollView:
    def print_grid(self, grid: Grid):
        for row in grid:
            print(*(tile.display for tile in row), sep = '')

    def print_remaining_moves(self, n: int):
        print(f'moves left: {n} ')

    def print_previous_moves(self, prev_moves: list[Arrow]):
        print('previous moves:', *prev_moves, sep = ' ')

    def print_points(self, n: int):
        print(f'points: ', n)

    def get_user_moves(self):
        return input('next move/s: ').strip().lower()
    
    def print_display(self, game_display: DisplayContent):
        self.print_grid(game_display.current_grid)
        self.print_previous_moves(game_display.previous_moves)
        self.print_remaining_moves(game_display.moves_left)
        self.print_points(game_display.points)

    def print_game_over_message(self):
        print('game over! ')

    def print_invalid_characters_message(self):
        print('no valid characters. please try again ')

    def clear_screen(self):
        if sys.stdout.isatty():
            clear_cmd = 'cls' if os.name == 'nt' else 'clear'
            os.system(clear_cmd)



