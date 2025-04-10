from project_types import Arrow, Order, Point
from tile import Egg, Grass, EmptyNest, OccupiedNest
from type_aliases import Grid


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
                            if self._current_grid[i][j].display is '🥚']

        self._previous_moves: list[Arrow] = []
        self._remaining_moves = move_count

    def _is_inside(self, row_num: int, col_num: int) -> bool:
        return 0 <= row_num < self._len_y and 0 <= col_num < self._len_x
    
    def roll(self, user_moves: list[Order]) -> Grid:
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
        
    def _rearrange_based_on_direction(self, coords: list[Point], direction: Order) -> list[Point]:
        match direction:
            case Order.RIGHT | Order.BACK:
                return coords[::-1]
            case _:
                return coords
                
    def _step_once(self, grid: Grid, user_move: Order) -> Grid:
        sorted_coords: list[Point] = self._rearrange_based_on_direction(self._egg_coords, user_move)
        
        resulting_grid = [list(row) for row in grid]
        surviving_egg_coords: list[Point] = []

        for point in sorted_coords:
            next_i, next_j = self._get_direction(user_move)
            next_i += point.x
            next_j += point.y
            next_point = Point(next_i, next_j)
            collided_tile = resulting_grid[next_i][next_j]

            if not self._is_inside(next_i, next_j):
                surviving_egg_coords.append(point)
                continue

            if collided_tile.will_block_egg:
                surviving_egg_coords.append(point)
            else:
                resulting_grid[next_i][next_j] = Egg(next_point)
                resulting_grid[point.x][point.y] = Grass(point)
                surviving_egg_coords.append(next_point)

            if collided_tile.will_eat_egg:
                assert not collided_tile.will_block_egg
                self._points += collided_tile.points_added
                resulting_grid[point.x][point.y] = Grass(point)

                # may not be good OCP-wise
                if isinstance(resulting_grid[next_i][next_j], EmptyNest):
                    resulting_grid[next_i][next_j] = OccupiedNest(next_point)

        return tuple(tuple(row) for row in resulting_grid)
    
    def _get_direction(self, user_move: Order) -> tuple[int, int]:
        match user_move:
            case Order.FRONT:
                return 0, -1
            case Order.BACK:
                return 0, 1
            case Order.LEFT:
                return -1, 0
            case Order.RIGHT:
                return 1, 0


    

            
