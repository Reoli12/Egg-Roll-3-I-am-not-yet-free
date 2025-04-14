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
        self._egg_coords = [Point(i, j) for i in range(self._len_y) for j in range(self._len_x)
                            if self._is_inside(i, j) and self._current_grid[i][j].display == '🥚']
        print(self._egg_coords)

        self._previous_moves: list[Arrow] = []
        self._remaining_moves = move_count

    @property
    def current_points(self):
        return self._points
    
    @property
    def previous_moves(self):
        return tuple(arrow.value for arrow in self._previous_moves)

    @property
    # not sure if needed, because the Grid type is immutable anyway.
    def current_grid(self):
        return self._current_grid
    
    @property
    def moves_left(self):
        return self._remaining_moves

    def _is_inside(self, row_num: int, col_num: int) -> bool:
        return 0 <= row_num < self._len_y and 0 <= col_num < self._len_x
    
    def roll(self, user_moves: list[Order]) -> Grid:
        if not user_moves:
            raise ValueError('should not happen! ')
        
        resulting_grid: Grid = self._current_grid
        for order in user_moves:
            resulting_grid = self._process_one_move(resulting_grid, order)
            self._previous_moves.append(order.value)
            self._remaining_moves -= 1
            
        return resulting_grid
    
    def _process_one_move(self, grid: Grid, user_move: Order) -> Grid:
        current_grid = grid
        while self._egg_coords:
            # print('still in loop')
            print(self._egg_coords)
            grid_eggs_next_step = self._step_once(current_grid, user_move)
            # actual bug: HOLY SHIT THE INPUT ABOVE WAS grid INSTEAD OF current_grid!!
            if current_grid == grid_eggs_next_step:
                break
            current_grid = grid_eggs_next_step
        return current_grid
        
    def _step_once(self, grid: Grid, user_move: Order) -> Grid:
        sorted_coords: list[Point] = self._rearrange_based_on_direction(self._egg_coords, user_move)
        
        resulting_grid = [list(row) for row in grid]
        surviving_egg_coords: list[Point] = []

        for point in sorted_coords:

            assert isinstance(resulting_grid[point.i][point.j], Egg)

            print(point)
            print(resulting_grid[point.i][point.j].display)
            next_i, next_j = self._get_direction(user_move)
            next_i += point.i
            next_j += point.j
            next_point = Point(next_i, next_j)
            collided_tile = resulting_grid[next_i][next_j]

            match collided_tile.will_block_egg, collided_tile.will_eat_egg:
                case True, False:
                    surviving_egg_coords.append(point)

                case False, False:
                    resulting_grid[next_i][next_j] = Egg(next_point)
                    resulting_grid[point.i][point.j] = Grass(point)
                    surviving_egg_coords.append(next_point)

                case False, True:
                    self._points += collided_tile.points_added
                    resulting_grid[point.i][point.j] = Grass(point)

                    # may not be good OCP-wise
                    if isinstance(resulting_grid[next_i][next_j], EmptyNest):
                        resulting_grid[next_i][next_j] = OccupiedNest(next_point)

                case _:
                    assert False, 'should not reach here! (logic problem)'
        
        self._egg_coords = list(_ for _ in surviving_egg_coords)

        print(*((''.join(tuple(tile.display for tile in row))) for row in resulting_grid), sep = '\n')
        return tuple(tuple(row) for row in resulting_grid)
    
    def _rearrange_based_on_direction(self, coords: list[Point], direction: Order) -> list[Point]:
        match direction:
            case Order.RIGHT:
                return coords[::-1]
            case Order.BACK:
                return sorted(coords, reverse= True, key = lambda point: point.i)
            case _:
                return coords
            
    def _get_direction(self, user_move: Order) -> tuple[int, int]:
        match user_move:
            case Order.FRONT:
                return -1, 0
            case Order.BACK:
                return 1, 0
            case Order.LEFT:
                return 0, -1
            case Order.RIGHT:
                return 0, 1

    

            
