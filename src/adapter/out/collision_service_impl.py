import math

from src.domain.model.map import Map
from src.domain.model.position import Position
from src.domain.model.vector import Vector
from src.domain.port.out.coliision_service_port import CollisionServicePort


class CollisionServiceImpl(CollisionServicePort):

    def position_to_tile(self, pos: Position) -> tuple[int, int]:
        tile_x = math.floor(pos.x)
        tile_y = math.floor(pos.y)
        return tile_x, tile_y

    def is_traversable(self, map_obj: Map, pos: Position) -> bool:
        tile_x, tile_y = self.position_to_tile(pos)
        tile = map_obj.get_tile(tile_x, tile_y)
        return not tile.is_solid()

    def try_move(self, map_obj: Map, pos: Position, vector: Vector) -> tuple[Position, bool]:
        new_pos = pos.add_vector(vector)
        if self.is_traversable(map_obj, new_pos):
            return new_pos, True
        return pos, False
