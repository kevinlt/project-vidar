from src.domain.model.map import Map
from src.domain.model.position import Position
from src.domain.service.coliision_service import CollisionService


class TestCollisionService:

    def test_cross_position_if_tile_is_not_solid(self):
        map = Map(10, 10)
        pos = Position(5.2, 5.)
        assert CollisionService.is_traversable(map, pos) == True