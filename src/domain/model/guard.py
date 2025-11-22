from src.domain.model.player import Player
from src.domain.model.position import Position


class Guard(Player):

    patrol_points: list[Position]
    current_patrol_index: int
    patrol_radius: float = .5
    vision_angle: int = 60

    def __init__(self, vision_angle: int = 60):
        super().__init__()
        self.current_patrol_index = 0
        self.patrol_points = []
        if vision_angle < 1 or vision_angle > 360:
            raise ValueError("Vision angle must be between 1 and 360 degrees")