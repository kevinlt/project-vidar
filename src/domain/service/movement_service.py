import math

from src.domain.model.player import Player
from src.domain.model.position import Position


class MovementService:

    @staticmethod
    def calculate_target_angle(player: Player, target_position: Position) -> float:
        return math.atan2(target_position.y - player.position.y, target_position.x - player.position.x)