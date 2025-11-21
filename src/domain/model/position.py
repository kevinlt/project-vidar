import math

from src.domain.model.vector import Vector


class Position:

    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, pos2: 'Position') -> float:
        return  math.sqrt((self.x - pos2.x) ** 2 + (self.y - pos2.y) ** 2)

    def add_vector(self, vector: Vector) -> 'Position':
        return Position(self.x + vector.dx, self.y + vector.dy)

    def substract_position(self, pos2: 'Position') -> Vector:
        return Vector(self.x - pos2.x, self.y - pos2.y)