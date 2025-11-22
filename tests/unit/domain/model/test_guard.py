import pytest

from src.domain.model.guard import Guard
from src.domain.model.position import Position


class TestGuard:

    def test_guard_has_player_properties(self):
        guard = Guard()
        assert guard.position is not None
        assert guard.direction is not None
        assert guard.velocity is not None
        assert guard.acceleration is not None
        assert guard.max_speed is not None
        assert guard.friction is not None
        assert guard.slip_factor is not None
        assert guard.turn_rate is not None

    def test_guard_has_patrol_points(self):
        guard = Guard()
        assert guard.patrol_points is not None

    def test_guard_try_to_move_to_next_patrol_point(self):
        guard = Guard()
        patrol_points = [
            Position(1., 1.),
            Position(2., 2.)
        ]
        guard.patrol_points = patrol_points
        assert guard.current_patrol_index == 0

    def test_guard_has_vision_angle(self):
        guard = Guard()
        assert guard.vision_angle is not None

    def test_guard_vision_angle_is_not_lower_1(self):
        with pytest.raises(ValueError):
            Guard(0)

    def test_guard_vision_angle_is_not_greater_360(self):
        with pytest.raises(ValueError):
            Guard(361)