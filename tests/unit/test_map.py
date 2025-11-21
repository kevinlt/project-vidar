from src.domain.model.map import Map
from src.domain.model.tile import Tile
from src.domain.model.tile_type import TileType


class TestMap:

    def test_map_is_a_grid_of_width_and_height(self):
        map = Map(10, 10)
        assert (map.width, map.height) == (10, 10)

    def test_get_map_tile_at_position_out_of_bounds_return_tile_outside_map(self):
        map = Map(10, 10)
        assert map.get_tile(-1,0).tile_type == TileType.OUTSIDE_MAP

    def test_get_map_tile_at_position_in_bounds_return_tile_inside_map(self):
        tiles = [[Tile(TileType.WALL), Tile(TileType.FLOOR)]]
        map = Map(10, 10)
        map.tiles = tiles
        assert map.get_tile(0,0).tile_type == TileType.WALL
