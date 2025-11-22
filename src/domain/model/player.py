from src.domain.model.position import Position


class Player:

    position: Position
    direction: float = 0.0
    turn_rate: float = 0.01

    def __init__(self, position: Position = None):
        if position is None:
            position = Position(0., 0.)
        self.position = position