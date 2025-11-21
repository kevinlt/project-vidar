from src.domain.model.vector import Vector


class TestVector:

    def test_vector_has_dx_and_dy(self):
        vector = Vector(1.0,2.0)
        assert vector.dx == 1.0
        assert vector.dy == 2.0

    def test_vector_should_give_length(self):
        vector = Vector(1.0, 2.0)
        assert vector.length() == 2.23606797749979

    def test_normalize_null_vector_gives_null_vector(self):
        vector = Vector(0.0, 0.0)
        normalizedVector = vector.normalize()
        assert normalizedVector.dx == 0.0
        assert normalizedVector.dy == 0.0