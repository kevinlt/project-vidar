from src.domain.model.position import Position
class TestPosition:

    def test_position_has_x_and_y(self):
        position = Position(1.0,2.0)
        assert position.x == 1.0
        assert position.y == 2.0