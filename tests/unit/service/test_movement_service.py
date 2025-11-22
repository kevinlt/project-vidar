from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.service.movement_service import MovementService


class TestMovementService:

    def test_target_angle_should_return_0_if_target_position_is_current_position(self):
        player = Player()
        player.direction = 0.0
        target_angle = MovementService.calculate_target_angle(player, Position(0., 0.))
        assert target_angle == 0.0