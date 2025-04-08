from project_types import Tile, Arrow, Order, Grid, Point


class EggRollModel:
    def __init__(self, grid: Grid, move_count: int) -> None:
        if not grid:
            raise ValueError('Grid does not exist ')
        if move_count <= 0:
            raise ValueError('Must have a positive amount of moves! ')
        
        self._points = 0
        self._previous_moves = []
        self._current_grid = grid
        self._len_y = len(self._current_grid)
        self._len_x = len(self._current_grid[0])
        self._egg_coords = [Point(i, j) for i in range(self._len_x) for j in range(self._len_y)
                            if self._current_grid[i][j] is Tile.EGG]
        
        self._previous_moves: list[Arrow] = []
        self._remaining_moves = move_count

    def _is_inside(self, row_num: int, col_num: int) -> bool:
        return 0 <= row_num < self._len_y and 0 <= col_num <= self._len_x
    
    def process_moves(self, user_moves: list[Order]) -> Grid:
        if not user_moves:
            raise ValueError('should not happen! ')
        
        resulting_grid: Grid = self._current_grid
        for order in user_moves:
            resulting_grid = self._process_one_move(resulting_grid, order)
            
        return resulting_grid
    
    def _process_one_move(self, grid: Grid, user_move: Order) -> Grid:
        current_grid = grid
        while True:
            grid_eggs_next_step = self._step_once(grid, user_move)
            if current_grid == grid_eggs_next_step:
                break
        return current_grid
        
    def _sort_based_on_direction(self, coords: list[Point], ) -> list[Point]:
        ...

    def _step_once(self, grid: Grid, user_move: Order) -> Grid:
        sorted_coords: list[Point] = self._sort_based_on_direction(self._egg_coords)
        ...
    

            
