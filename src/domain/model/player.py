from src.domain.model.position import Position

class Player:

    position: Position
    velocity: float = 0.0
    max_speed: float = 1.0
    acceleration: float = 0.01
    direction: float = 0.0
    turn_rate: float = 0.01
    friction: float = 0.99
    slip_factor: float = 0.01

    def __init__(self, position: Position = None):
        if position is None:
            position = Position(0., 0.)
        self.position = position
