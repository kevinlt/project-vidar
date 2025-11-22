import math

from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.service.movement_service import MovementService


class TestMovementService:

    def test_target_angle_should_return_0_if_target_position_is_current_position(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player.position, Position(0., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_0_if_player_target_is_straight_right(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player.position, Position(5., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_pi_if_player_target_is_straight_left(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player.position, Position(-5., 0.))
        assert target_angle == math.pi

    def test_direction_is_limited_by_player_turn_rate(self):
        player = Player()
        player.turn_rate = 0.5
        target_angle = 1.5
        player.slip_factor = 0
        direction = MovementService.limit_rotation(player.direction, player.turn_rate, target_angle)
        assert direction == 0.5

    def test_movement_direction_is_altered_by_slip_factor(self):
        player = Player()
        target_angle = 1.5
        player.slip_factor = 0.5
        direction = MovementService.interpolate(player.direction, target_angle, player.slip_factor)
        assert direction == 0.75

    def test_velocity_is_limited_by_player_max_speed(self):
        player = Player()
        player.velocity = 0.5
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 1
        MovementService.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        assert player.velocity == 0.5

    def test_velocity_is_reduce_by_player_friction(self):
        player = Player()
        player.velocity = 1.
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 0.98
        velocity = MovementService.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        assert velocity == 0.98
