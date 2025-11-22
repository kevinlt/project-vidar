import math

from src.domain.model.map import Map
from src.domain.model.position import Position
from src.domain.model.vector import Vector


class CollisionService:

    @staticmethod
    def position_to_tile(pos: Position) -> tuple[int, int]:
        tile_x = math.floor(pos.x)
        tile_y = math.floor(pos.y)
        return tile_x, tile_y

    @staticmethod
    def is_traversable(map_obj: Map, pos: Position) -> bool:
        tile_x, tile_y = CollisionService.position_to_tile(pos)
        tile = map_obj.get_tile(tile_x, tile_y)
        return not tile.is_solid()

    @staticmethod
    def try_move(map_obj: Map, pos: Position, vector: Vector) -> Position:
        new_pos = pos.add_vector(vector)
        if CollisionService.is_traversable(map_obj, new_pos):
            return new_pos
        return pos
