from typing import Any

from src.domain.model.tile import Tile
from src.domain.model.tile_type import TileType


class Map:

    width: int
    height: int
    tiles: list

    def __init__(self, width: int, height: int, tiles=None):
        self.width = width
        self.height = height
        if tiles is not None:
            self.tiles = tiles
        else:
            # par défaut : une map vide (sol partout)
            self.tiles = [
                [Tile(TileType.FLOOR) for _ in range(width)]
                for _ in range(height)
            ]

    def is_inside(self, pos_x: int, pos_y:int) -> bool:
        return 0 <= pos_x < self.width and 0 <= pos_y < self.height

    def get_tile(self, pos_x: int, pos_y:int) -> Tile:
        if self.is_inside(pos_x, pos_y):
           return self.tiles[pos_y][pos_x]
        else:
            return Tile(TileType.OUTSIDE_MAP)