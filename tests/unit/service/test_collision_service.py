from src.domain.model.map import Map, Tile, TileType
from src.domain.model.position import Position
from src.domain.service.coliision_service import CollisionService

class TestCollisionService:

    def test_position_is_traversable_if_tile_is_not_solid(self):
        map = Map(10, 10)
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == True

    def test_position_is_not_traversable_if_tile_is_solid(self):
        map = Map(10, 10)
        map.set_tile(5,5, Tile(TileType.WALL))
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == False

    def test_position_is_not_traversable_if_outside_map(self):
        map = Map(10, 10)
        pos = Position(-1., 5.)
        assert CollisionService.is_traversable(map, pos) == False