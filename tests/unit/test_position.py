from src.domain.model.position import Position
class TestPosition:

    def test_position_has_x_and_y(self):
        position = Position(1.0,2.0)
        assert position.x == 1.0
        assert position.y == 2.0

    def test_position_should_give_distance_from_another_position(self):
        pos1 = Position(1.0,2.0)
        pos2 = Position(1.0,5.0)
        assert pos1.distance_to(pos2) == 3.0