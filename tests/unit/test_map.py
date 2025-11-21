from src.domain.model.map import Map
from src.domain.model.tile import Tile


class TestMap:

    def test_map_is_a_grid_of_width_and_height(self):
        map = Map(10, 10)
        assert (map.width, map.height) == (10, 10)

    def test_get_map_tile_at_position_out_of_bounds_return_tile_outside_map(self):
        map = Map(10, 10)
        assert map.get_tile(-1,0) == Tile.OUTSIDE_MAP