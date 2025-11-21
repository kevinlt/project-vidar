from src.domain.model.map import Map


class TestMap:

    def test_map_is_a_grid_of_width_and_height(self):
        map = Map(10, 10)
        assert (map.width, map.height) == (10, 10)