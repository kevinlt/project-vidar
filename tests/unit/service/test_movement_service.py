import math

from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.service.movement_service import MovementService


class TestMovementService:

    def test_target_angle_should_return_0_if_target_position_is_current_position(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player, Position(0., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_0_if_player_target_is_straight_right(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player, Position(5., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_pi_if_player_target_is_straight_left(self):
        player = Player()
        target_angle = MovementService.calculate_target_angle(player, Position(-5., 0.))
        assert target_angle == math.pi

    def test_direction_is_limited_by_player_turn_rate(self):
        player = Player()
        player.turn_rate = 0.5
        target_angle = 1.5
        direction = MovementService.calculate_direction(player, target_angle)
        assert direction == 0.5