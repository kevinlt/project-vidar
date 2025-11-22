from src.domain.model.player import Player


class TestPlayer:

    def test_player_has_position(self):
        player = Player()
        assert player.position is not None

    def test_player_position_is_mutable(self):
        player = Player()
        player.position.x = 10.
        assert player.position.x == 10.

    def test_player_has_direction(self):
        player = Player()
        assert player.direction is not None