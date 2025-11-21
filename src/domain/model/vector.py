import math

class Vector:

    dx: float
    dy: float
    magnitude_max: float

    def __init__(self, dx, dy, magnitude_max=5.0):
        self.dx = dx
        self.dy = dy
        self.magnitude_max = magnitude_max

        if self.length() > magnitude_max:
            self.normalize().multiply(magnitude_max)

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
        self.dx -= vector.dx
        self.dy -= vector.dy
        return self

    def angle_of(self, vector: 'Vector') -> float:
        return math.atan2(vector.dy, vector.dx) - math.atan2(self.dy, self.dx)

    def angle(self) -> float:
        return math.atan2(self.dy, self.dx)

    def from_angle_magnitude(self, angle: float, magnitude: float) -> 'Vector':
        self.dx = magnitude * math.cos(angle)
        self.dy = magnitude * math.sin(angle)
        return self

    def reverse(self) -> 'Vector':
        self.dx = -self.dx
        self.dy = -self.dy
        return self