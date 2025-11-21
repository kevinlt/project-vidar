import math

class Position:

    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, pos2):
        return  math.sqrt((self.x - pos2.x) ** 2 + (self.y - pos2.y) ** 2)