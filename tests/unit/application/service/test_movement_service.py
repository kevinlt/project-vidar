import math

from src.adapter.out.collision_service_impl import CollisionServiceImpl
from src.application.service.movement_service import MovementService
from src.domain.model.map import Map, Tile, TileType
from src.domain.model.player import Player
from src.domain.model.position import Position


class TestPlayerMovementService:

    movement_service = MovementService(CollisionServiceImpl())

    def test_target_angle_should_return_0_if_target_position_is_current_position(self):
        player = Player()
        target_angle = self.movement_service.calculate_target_angle(player.position, Position(0., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_0_if_player_target_is_straight_right(self):
        player = Player()
        target_angle = self.movement_service.calculate_target_angle(player.position, Position(5., 0.))
        assert target_angle == 0.

    def test_target_angle_should_return_pi_if_player_target_is_straight_left(self):
        player = Player()
        target_angle = self.movement_service.calculate_target_angle(player.position, Position(-5., 0.))
        assert target_angle == math.pi

    def test_direction_is_limited_by_player_turn_rate(self):
        player = Player()
        player.turn_rate = 0.5
        target_angle = 1.5
        player.slip_factor = 0
        direction = self.movement_service.limit_rotation(player.direction, player.turn_rate, target_angle)
        assert direction == 0.5

    def test_movement_direction_is_altered_by_slip_factor(self):
        player = Player()
        target_angle = 1.5
        player.slip_factor = 0.5
        direction = self.movement_service.interpolate(player.direction, target_angle, player.slip_factor)
        assert direction == 0.75

    def test_velocity_is_limited_by_player_max_speed(self):
        player = Player()
        player.velocity = 0.5
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 1
        self.movement_service.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        assert player.velocity == 0.5

    def test_velocity_is_reduce_by_player_friction(self):
        player = Player()
        player.velocity = 1.
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 0.98
        velocity = self.movement_service.update_velocity(player.velocity, player.acceleration, player.max_speed, player.friction)
        assert velocity == 0.98


    def test_player_should_move(self):
        map_obj = Map(10, 10)
        player = Player()
        player.position = Position(5., 5.)
        player.velocity = 1.
        player.acceleration = 1.
        player.max_speed = 1.
        player.friction = 1
        player.slip_factor = 0

        self.movement_service.update_player_position(player, map_obj, Position(10., 10.))
        assert  5.9 < player.position.x < 6.1

    def test_player_should_not_move(self):
        map_obj = Map(10, 10)
        player = Player()
        player.position = Position(5., 5.)
        player.velocity = 0.
        player.acceleration = 0.
        player.max_speed = 1.
        player.friction = 1
        self.movement_service.update_player_position(player, map_obj, Position(10., 10.))
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
        self.movement_service.update_player_position(player, map_obj, Position(10., 10.))
        assert player.position.x == 5.
        assert player.position.y == 5.
        assert player.velocity == 0.

    def test_player_has_reach_target(self):
        player = Player()
        player.position = Position(9.6, 10.)
        assert self.movement_service.has_reach_target(player.position, Position(10., 10.), 5.) == True