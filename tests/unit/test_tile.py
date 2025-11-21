from src.domain.model.tile import Tile
from src.domain.model.tile_type import TileType


class TestTile:

    def test_tile_is_solid(self):
        tile = Tile(TileType.WALL)
        assert tile.is_solid()