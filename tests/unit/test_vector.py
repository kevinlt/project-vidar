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

    def test_substract_vector(self):
        vector = Vector(2., 2.)
        vector.substract(Vector(1., 1.))
        assert vector.dx == 1.
        assert vector.dy == 1.

    def test_angle_between_vectors_is_0_if_a_vector_is_nul(self):
        vector = Vector(0., 0.)
        assert vector.angle_of(Vector(1., 0.)) == 0.

    def test_vector_should_have_max_magnitude_of_2(self):
        vector = Vector(3., 4., 2.)
        vector.normalize()
        assert vector.length() == 1.

    def test_vector_should_be_normalized_if_magnitude_exceeds_max_magnitude(self):
        vector = Vector(3., 4., 2.)
        assert vector.length() == 2.

    def test_reverse_vector(self):
        vector = Vector(5., 2.)
        vector.reverse()
        assert -4. > vector.dx > -6.
        assert -1. > vector.dy > -3.