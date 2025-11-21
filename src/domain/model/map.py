from enum import Enum

class TileType(Enum):

    OUTSIDE_MAP = 0
    FLOOR = 1
    WALL = 2

class Tile:

    tile_type: 'TileType'

    def __init__(self, tile_type: 'TileType'):
        self.tile_type = tile_type

    def is_solid(self) -> bool:
        return self.tile_type in [TileType.WALL, TileType.OUTSIDE_MAP]

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

    def get_tile(self, pos_x: int, pos_y:int) -> 'Tile':
        if self.is_inside(pos_x, pos_y):
           return self.tiles[pos_y][pos_x]
        else:
            return Tile(TileType.OUTSIDE_MAP)

    def set_tile(self, pos_x: int, pos_y:int, tile: Tile):
        if not self.is_inside(pos_x, pos_y):
            raise IndexError("Tuile hors de la map")
        self.tiles[pos_y][pos_x] = tile

    def is_solid(self, pos_x: int, pos_y:int) -> bool:
        return self.get_tile(pos_x, pos_y).is_solid()