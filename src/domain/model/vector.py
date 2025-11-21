import math


class Vector:

    dx: float
    dy: float

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def length(self) -> float:
        return math.sqrt(self.dx ** 2 + self.dy ** 2)
