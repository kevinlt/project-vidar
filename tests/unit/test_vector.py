from src.domain.model.vector import Vector


class TestVector:

    def test_vector_has_dx_and_dy(self):
        vector = Vector(1.0,2.0)
        assert vector.dx == 1.0
        assert vector.dy == 2.0