import math

from src.domain.model.player import Player
from src.domain.model.position import Position


class MovementService:

    @staticmethod
    def calculate_target_angle(player: Player, target_position: Position) -> float:
        return math.atan2(target_position.y - player.position.y, target_position.x - player.position.x)

    @staticmethod
    def calculate_direction(player: Player, target_angle: float) -> float:
        delta = MovementService.normalize_angle(target_angle - player.direction)
        rotation = MovementService.clamp(delta, -player.turn_rate, player.turn_rate)
        return player.direction + rotation

    @staticmethod
    def normalize_angle(angle: float) -> float:
        return angle % (2 * math.pi)

    @staticmethod
    def clamp(target_angle: float, min_angle: float, max_angle: float) -> float:
        return min(max(target_angle, min_angle), max_angle)