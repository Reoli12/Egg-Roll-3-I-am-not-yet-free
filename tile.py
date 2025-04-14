from abc import ABC
from dataclasses import dataclass
from point import Point

@dataclass
class Tile(ABC):
    coords: Point
    display: str
    will_block_egg: bool 
    will_eat_egg: bool
    points_added: int

@dataclass
class Egg(Tile):
    display: str= '🥚'
    will_block_egg: bool= True
    will_eat_egg: bool= False
    points_added: int= 0
    
@dataclass
class Wall(Tile):
    display: str= '🧱'
    will_block_egg: bool= True
    will_eat_egg: bool= False
    points_added: int= 0

@dataclass
class Grass(Tile):
    display: str = '🟩'
    will_block_egg: bool = False
    will_eat_egg: bool = False
    points_added: int = 0

@dataclass
class Pan(Tile):
    display: str= '🍳'
    will_block_egg: bool= False
    will_eat_egg: bool= True
    points_added: int= -10

@dataclass
class EmptyNest(Tile):
    display: str= '🪹'
    will_block_egg: bool= False
    will_eat_egg: bool= True
    points_added: int= 10

@dataclass
class OccupiedNest(Tile):
    display: str= '🪺'
    will_block_egg: bool= True
    will_eat_egg: bool= False
    points_added: int= 0

tile_classes = (Egg, EmptyNest, Grass, OccupiedNest, Pan, Wall)