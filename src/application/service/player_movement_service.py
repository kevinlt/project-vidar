from src.domain.model.map import Map
from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.service.coliision_service import CollisionService
from src.domain.service.movement_service import MovementService


class PlayerMovementService:

    collision_service: CollisionService

    def __init__(self, collision_service: CollisionService):
        self.collision_service = collision_service

    def update_player_position(self, player: Player, map_obj: Map, target: Position):
        target_angle = MovementService.calculate_target_angle(player.position, target)
        player.direction = MovementService.limit_rotation(player.direction, target_angle, player.turn_rate)
        player.velocity = MovementService.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        move_vector = MovementService.compute_movement_vector(player.position, target, player.direction, player.velocity, player.slip_factor)
        new_position, moved = self.collision_service.try_move(map_obj, player.position, move_vector)
        player.position = new_position
        if not moved:
            player.velocity = 0
