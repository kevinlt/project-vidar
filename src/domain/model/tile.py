from src.domain.model.tile_type import TileType


class Tile:

    tile_type: TileType

    def __init__(self, tile_type: TileType):
        self.tile_type = tile_type

    def is_solid(self) -> bool:
        if self.tile_type == TileType.WALL:
            return True
        return False