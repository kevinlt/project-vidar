from src.domain.model.guard import Guard
from src.domain.model.position import Position
from src.domain.port.out.collision_service_port import CollisionServicePort


class GuardAiService:

    collision_service: CollisionServicePort

    def __init__(self, collision_service: CollisionServicePort):
        self.collision_service = collision_service

    def has_reach_target(self, position:Position, target: Position, patrol_radius: float):
        return position.distance_to(target) < patrol_radius

