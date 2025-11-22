import math

from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.model.vector import Vector


class MovementService:

    @staticmethod
    def calculate_target_angle(position: Position, target_position: Position) -> float:
        return math.atan2(target_position.y - position.y, target_position.x - position.x)

    @staticmethod
    def normalize_angle(angle: float) -> float:
        return angle % (2 * math.pi)

    @staticmethod
    def clamp(target_angle: float, min_angle: float, max_angle: float) -> float:
        return min(max(target_angle, min_angle), max_angle)

    @staticmethod
    def interpolate(direction: float, target_angle: float, factor: float) -> float:
        return direction + factor * (target_angle - direction)

    @staticmethod
    def limit_rotation(direction: float, turn_rate: float, target_angle: float) -> float:
        delta = MovementService.normalize_angle(target_angle - direction)
        rotation = MovementService.clamp(delta, -turn_rate, turn_rate)
        direction = direction + rotation
        return direction

    @staticmethod
    def update_velocity(velocity: float, acceleration: float, max_speed: float, friction: float) -> float:
        velocity = min(max_speed, velocity + acceleration)
        velocity *= friction
        return velocity

    @staticmethod
    def compute_movement_vector(position: Position, target: Position, direction: float, velocity: float, slip_factor: float) -> Vector:
        target_angle = MovementService.calculate_target_angle(position, target)
        direction = MovementService.interpolate(direction, target_angle, slip_factor)
        dx = math.cos(direction) * velocity
        dy = math.sin(direction) * velocity
        return Vector(dx, dy)
