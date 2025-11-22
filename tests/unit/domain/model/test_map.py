from logging import raiseExceptions

import pytest

from src.domain.model.map import Map, Tile, TileType


class TestMap:

    def test_map_is_a_grid_of_width_and_height(self):
        map = Map(10, 10)
        assert (map.width, map.height) == (10, 10)

    def test_get_map_tile_at_position_out_of_bounds_return_tile_outside_map(self):
        map = Map(10, 10)
        assert map.get_tile(-1,0).tile_type == TileType.OUTSIDE_MAP

    def test_get_map_tile_at_position_in_bounds_return_tile_inside_map(self):
        tiles = [[Tile(TileType.WALL), Tile(TileType.FLOOR)]]
        map = Map(10, 10, tiles)
        assert map.get_tile(0,0).tile_type == TileType.WALL

    def test_tile_is_solid(self):
        tiles = [[Tile(TileType.WALL), Tile(TileType.FLOOR)]]
        map = Map(10, 10, tiles)
        assert map.is_solid(0,0) == True

    def test_cannot_set_tile_outside_map(self):
        map = Map(10, 10)
        with pytest.raises(IndexError):
            map.set_tile(-1,0, Tile(TileType.WALL))