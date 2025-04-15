from project_types import Arrow, DisplayContent, Grid, Feedback, Order, RunningStatus
from tile import Egg, Grass, EmptyNest, OccupiedNest
from point import Point

class EggRollModel:
    def __init__(self, grid: Grid, move_count: int) -> None:
        if not grid:
            raise ValueError('Grid does not exist ')
        if move_count <= 0:
            raise ValueError('Must have a positive amount of moves! ')
        
        self._points = 0
        self._current_grid = grid
        self._len_y = len(self._current_grid)
        self._len_x = len(self._current_grid[0])
        self._egg_coords = [Point(i, j) for i in range(self._len_y) for j in range(self._len_x)
                            if self._is_inside(i, j) and self._current_grid[i][j].display == '🥚']

        self._previous_moves: list[Arrow] = []
        self._remaining_moves = move_count

        self._movement_frames: list[DisplayContent] | None = None
    
    @property
    def moves_left(self):
        return self._remaining_moves
    
    @property
    def previous_moves(self):
        return tuple(self._previous_moves)
    
    @property
    def running_status(self):
        return (RunningStatus.ONGOING if self._egg_coords and self._remaining_moves > 0 
        else RunningStatus.DONE)
            
    @property
    def display_content(self):
        return DisplayContent(
            self._current_grid,
            self.previous_moves,
            self._remaining_moves,
            self._points
        )
    
    @property
    def movement_frames(self):
        assert self._movement_frames is not None, 'should be a list'
        return tuple(self._movement_frames)

    def _is_inside(self, row_num: int, col_num: int) -> bool:
        return 0 <= row_num < self._len_y and 0 <= col_num < self._len_x
    
    def roll(self, user_moves: list[Order]) -> Grid:
        if not user_moves:
            raise ValueError('should not happen! ')
        
        assert self._movement_frames is None, 'should have been cleared before this'
        self._movement_frames = []

        resulting_grid: Grid = self._current_grid
        for order in user_moves:
            if self.running_status is not RunningStatus.DONE:
                self._previous_moves.append(order.value)
                self._remaining_moves -= 1
                resulting_grid = self._process_one_move(resulting_grid, order)
                
            

        #update grid here: current bug is current grid reverts to initial grid after roll finishes
        self._current_grid = resulting_grid   
        return resulting_grid
    
    def _process_one_move(self, grid: Grid, user_move: Order) -> Grid:
        
        assert isinstance(self._movement_frames, list), 'should have been initialized as such before'

        current_grid = grid
        while True:
            grid_eggs_next_step = self._step_once(current_grid, user_move)
            # actual bug: HOLY SHIT THE INPUT ABOVE WAS grid INSTEAD OF current_grid!!
            if current_grid == grid_eggs_next_step:
                break
            current_grid = grid_eggs_next_step
            current_game_state = DisplayContent(
                current_grid, self.previous_moves, self._remaining_moves, self._points
            )
            self._movement_frames.append(current_game_state)

        return current_grid
        
    def _step_once(self, grid: Grid, user_move: Order) -> Grid:
        sorted_coords: list[Point] = self._rearrange_based_on_direction(self._egg_coords, user_move)
        
        resulting_grid = [list(row) for row in grid]
        surviving_egg_coords: list[Point] = []

        for point in sorted_coords:

            assert isinstance(resulting_grid[point.i][point.j], Egg), f'({point.i}, {point.j})'

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
                        self._points += self._remaining_moves

                case _:
                    assert False, 'should not reach here! (logic problem)'
        
        self._egg_coords = list(_ for _ in surviving_egg_coords)

        return tuple(tuple(row) for row in resulting_grid)
    
    def reset_movement_frames(self):
        ''' should be run after every self.roll '''
        self._movement_frames = None
    
    def _rearrange_based_on_direction(self, coords: list[Point], direction: Order) -> list[Point]:
        match direction:
            case Order.RIGHT:
                return sorted(coords, reverse= True, key = lambda point: point.j)
            case Order.BACK:
                return sorted(coords, reverse= True, key = lambda point: point.i)
            case Order.LEFT:
                return sorted(coords, key = lambda point: point.j)
            case Order.FRONT:
                return sorted(coords, key = lambda point: point.i)
            
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
            
    def get_feedback(self, orders: str) -> Feedback:
        valid_orders = set(('f', 'b', 'l', 'r'))
        order_chars = set(orders)

        if not valid_orders & order_chars:
            return Feedback.INVALID
        return Feedback.VALID
    
    def parse_user_moves(self, user_moves: str):
        char_to_order_mapping = {
            'l' : Order.LEFT,
            'r' : Order.RIGHT,
            'f' : Order.FRONT,
            'b' : Order.BACK
        }
        res: list[Order] = []

        for char in user_moves:
            if char in char_to_order_mapping:
                res.append(char_to_order_mapping[char])
        return res

    

            
