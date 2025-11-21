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
            self.dx = 0.
            self.dy = 0.
            return self
        return self.multiply(1. / self.length())

    def multiply(self, scalar: float) -> 'Vector':
        self.dx *= scalar
        self.dy *= scalar
        return self

    def add(self, vector: 'Vector') -> 'Vector':
        self.dx += vector.dx
        self.dy += vector.dy
        return self

    def substract(self, vector: 'Vector') -> 'Vector':
        self.dx = max(0., self.dx - vector.dx)
        self.dy = max(0., self.dy - vector.dy)
        return self

