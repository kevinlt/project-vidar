from src.adapter.out.collision_service_impl import CollisionServiceImpl
from src.application.service.guard_movement_service import GuardMovementService
from src.domain.model.guard import Guard
from src.domain.model.map import Map
from src.domain.model.position import Position


class TestGuardMovementService:

    def test_guard_movement_service_has_collision_service(self):
        collision_service = CollisionServiceImpl()
        guard_movement_service = GuardMovementService(collision_service)
        assert guard_movement_service.collision_service is not None

    def test_guard_movement_service_reaches_target_position(self):
        guard = Guard()
        guard.patrol_points = [Position(10., 10.), Position(11., 11.)]
        guard.position = Position(9.6, 10.)
        guard_movement_service = GuardMovementService(CollisionServiceImpl())
        assert guard_movement_service.has_reach_target(guard.position, guard.patrol_points[guard.current_patrol_index], guard.patrol_radius) == True

    def test_guard_current_patrol_index_is_next_when_target_is_reached(self):
        guard = Guard()
        guard.patrol_points = [Position(10., 10.), Position(11., 11.)]
        guard.current_patrol_index = 0
        guard.position = Position(9.6, 10.)
        guard_movement_service = GuardMovementService(CollisionServiceImpl())
        map_obj = Map(10, 10)
        guard_movement_service.update_guard_position(guard, map_obj)
        assert guard.current_patrol_index == 1