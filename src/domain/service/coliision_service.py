import math

from src.domain.model.map import Map
from src.domain.model.position import Position


class CollisionService:

    @staticmethod
    def is_traversable(map: Map, pos: Position) -> bool:
        tile_x = math.floor(pos.x)
        tile_y = math.floor(pos.y)
        return not map.is_solid(tile_x, tile_y)