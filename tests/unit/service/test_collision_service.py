from src.domain.model.map import Map, Tile, TileType
from src.domain.model.position import Position
from src.domain.model.vector import Vector
from src.domain.service.coliision_service import CollisionService

class TestCollisionService:

    def define_map(self) -> Map:
        map = Map(10, 10)
        return map

    def test_position_is_traversable_if_tile_is_not_solid(self):
        map = self.define_map()
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == True

    def test_position_is_not_traversable_if_tile_is_solid(self):
        map = self.define_map()
        map.set_tile(5,5, Tile(TileType.WALL))
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == False

    def test_position_is_not_traversable_if_outside_map(self):
        map = self.define_map()
        pos = Position(-1., 5.)
        assert CollisionService.is_traversable(map, pos) == False

    def test_try_to_move_should_gives_new_position_if_succeed(self):
        map = self.define_map()
        pos = Position(1., 1.)
        vector = Vector(1., 1.)
        assert isinstance(CollisionService.try_move(map, pos, vector), Position)

    def test_try_to_move_should_return_same_position_if_failed(self):
        map = self.define_map()
        pos = Position(1., 1.)
        vector = Vector(10., 10., 20)
        new_pos = CollisionService.try_move(map, pos, vector)
        assert pos.x == new_pos.x
        assert pos.y == new_pos.y
