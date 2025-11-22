from src.application.service.player_movement_service import PlayerMovementService
from src.domain.model.map import Map, Tile, TileType
from src.domain.model.player import Player
from src.domain.model.position import Position
from src.domain.service.coliision_service import CollisionService


class TestPlayerMovementService:

    def test_player_should_move(self):
        map_obj = Map(10, 10)
        player = Player()
        player.position = Position(5., 5.)
        player.velocity = 1.
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 1
        player.slip_factor = 0

        movement_service = PlayerMovementService(CollisionService())
        movement_service.update_player_position(player, map_obj, Position(10., 10.))
        assert  5.9 < player.position.x < 6.1

    def test_player_should_not_move(self):
        map_obj = Map(10, 10)
        player = Player()
        player.position = Position(5., 5.)
        player.velocity = 0.
        player.acceleration = 0.
        player.max_speed = 1.
        player.friction = 1
        movement_service = PlayerMovementService(CollisionService())
        movement_service.update_player_position(player, map_obj, Position(10., 10.))
        assert player.position.x == 5.
        assert player.position.y == 5.

    def test_player_should_not_move_if_collision(self):
        map_obj = Map(10, 10)
        map_obj.set_tile(6,5, Tile(TileType.WALL))
        map_obj.set_tile(5,6, Tile(TileType.WALL))
        player = Player()
        player.position = Position(5., 5.)
        player.velocity = 2.
        player.acceleration = 1.
        player.max_speed = 2.
        player.friction = 1
        movement_service = PlayerMovementService(CollisionService())
        movement_service.update_player_position(player, map_obj, Position(10., 10.))
        assert player.position.x == 5.
        assert player.position.y == 5.
        assert player.velocity == 0.