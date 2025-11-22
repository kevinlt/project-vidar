from src.domain.model.player import Player
from src.domain.model.position import Position


class Guard(Player):

    patrol_points: list[Position]
    current_patrol_index: int
    patrol_radius: float = .5

    def __init__(self):
        super().__init__()
        self.current_patrol_index = 0
        self.patrol_points = []
