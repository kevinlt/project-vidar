import math

from src.domain.model.map import Map
from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.model.vector import Vector
from src.domain.port.out.coliision_service_port import CollisionServicePort


class MovementService:

    collision_service: CollisionServicePort

    def __init__(self, collision_service: CollisionServicePort):
        self.collision_service = collision_service

    def update_player_position(self, player: Player, map_obj: Map, target: Position):
        target_angle = self.calculate_target_angle(player.position, target)
        player.direction = self.limit_rotation(player.direction, target_angle, player.turn_rate)
        player.velocity = self.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        move_vector = self.compute_movement_vector(player.position, target, player.direction, player.velocity, player.slip_factor)
        new_position, moved = self.collision_service.try_move(map_obj, player.position, move_vector)
        player.position = new_position
        if not moved:
            player.velocity = 0


    def calculate_target_angle(self, position: Position, target_position: Position) -> float:
        return math.atan2(target_position.y - position.y, target_position.x - position.x)

    def normalize_angle(self, angle: float) -> float:
        return angle % (2 * math.pi)

    def clamp(self, target_angle: float, min_angle: float, max_angle: float) -> float:
        return min(max(target_angle, min_angle), max_angle)

    def interpolate(self, direction: float, target_angle: float, factor: float) -> float:
        return direction + factor * (target_angle - direction)

    def limit_rotation(self, direction: float, turn_rate: float, target_angle: float) -> float:
        delta = self.normalize_angle(target_angle - direction)
        rotation = self.clamp(delta, -turn_rate, turn_rate)
        direction = direction + rotation
        return direction

    def update_velocity(self, velocity: float, acceleration: float, max_speed: float, friction: float) -> float:
        velocity = min(max_speed, velocity + acceleration)
        velocity *= friction
        return velocity

    def compute_movement_vector(self, position: Position, target: Position, direction: float, velocity: float, slip_factor: float) -> Vector:
        target_angle = self.calculate_target_angle(position, target)
        direction = self.interpolate(direction, target_angle, slip_factor)
        dx = math.cos(direction) * velocity
        dy = math.sin(direction) * velocity
        return Vector(dx, dy)

