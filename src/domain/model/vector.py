import math

class Vector:

    dx: float
    dy: float

    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def length(self) -> float:
        return math.sqrt(self.dx ** 2 + self.dy ** 2)

    def normalize(self) -> 'Vector':
        if self.length() == 0:
            return Vector(0., 0.)
        return Vector(self.dx / self.length(), self.dy / self.length())

    def multiply(self, scalar: float) -> 'Vector':
        return Vector(self.dx * scalar, self.dy * scalar)
