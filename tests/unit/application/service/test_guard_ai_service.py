from src.adapter.out.collision_service_impl import CollisionServiceImpl
from src.application.service.guard_ai_service import GuardAiService
from src.domain.model.guard import Guard
from src.domain.model.position import Position


class TestGuardAiService:

    def test_guard_ai_service_has_collision_service(self):
        collision_service = CollisionServiceImpl()
        guard_ai_service = GuardAiService(collision_service)
        assert guard_ai_service.collision_service is not None

    def test_guard_ai_service_reaches_target_position(self):
        guard = Guard()
        guard.position = Position(9.6, 10.)
        target = Position(10., 10.)
        guard_ai_service = GuardAiService(CollisionServiceImpl())
        assert guard_ai_service.has_reach_target(guard.position, target, guard.patrol_radius) == True
