# another quick fix for circular imports

from dataclasses import dataclass

@dataclass
class Point:
    i: int
    j: int
