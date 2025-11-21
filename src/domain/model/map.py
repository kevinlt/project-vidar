from src.domain.model.tile import Tile


class Map:

    width: int
    height: int

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_tile(self, pos_x: int, pos_y:int):
        if pos_x < 0 or pos_x >= self.width or pos_y < 0 or pos_y >= self.height:
            return Tile.OUTSIDE_MAP