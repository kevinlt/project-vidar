from src.application.service.movement_service import MovementService
from src.domain.model.guard import Guard
from src.domain.model.map import Map
from src.domain.model.position import Position
from src.domain.port.out.collision_service_port import CollisionServicePort


class GuardAiService(MovementService):

    collision_service: CollisionServicePort

    def __init__(self, collision_service: CollisionServicePort):
        super().__init__(collision_service)

    def update_guard_position(self, guard: Guard, map_obj: Map) -> Position:
        super().update_player_position(guard, map_obj, guard.patrol_points[guard.current_patrol_index])
        patrol_point_reached = self.has_reach_target(guard.position, guard.patrol_points[guard.current_patrol_index], guard.patrol_radius)
        if patrol_point_reached:
            guard.current_patrol_index = self.update_patrol_index(guard)
        return guard.patrol_points[guard.current_patrol_index]

    def update_patrol_index(self, guard: Guard) -> int:
        return (guard.current_patrol_index + 1) % len(guard.patrol_points)

    def has_reach_target(self, position:Position, target: Position, patrol_radius: float) -> bool:
        return position.distance_to(target) < patrol_radius

