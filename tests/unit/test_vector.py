from src.domain.model.vector import Vector


class TestVector:

    def test_vector_has_dx_and_dy(self):
        vector = Vector(1.,2.)
        assert vector.dx == 1.
        assert vector.dy == 2.

    def test_vector_should_give_length(self):
        vector = Vector(1., 2.)
        assert vector.length() == 2.23606797749979

    def test_normalize_null_vector_gives_null_vector(self):
        vector = Vector(0., 0.)
        vector.normalize()
        assert vector.dx == 0.
        assert vector.dy == 0.

    def test_normalize_vector_gives_unit_vector(self):
        vector = Vector(3., 4.)
        vector.normalize()
        assert vector.length() == 1.

    def test_multiply_vector_by_scalar_return_new_vector(self):
        vector = Vector(1., 1.)
        vector.multiply(2.)
        assert vector.dx == 2.
        assert vector.dy == 2.

    def test_add_vector(self):
        vector = Vector(1., 1.)
        vector.add(Vector(2., 2.))
        assert vector.dx == 3.
        assert vector.dy == 3.