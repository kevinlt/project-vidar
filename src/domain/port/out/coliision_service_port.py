from abc import abstractmethod, ABC

class CollisionServicePort(ABC):

    @abstractmethod
    def position_to_tile(self,  pos):
        pass

    @abstractmethod
    def is_traversable(self, map_obj, pos):
        pass

    @abstractmethod
    def try_move(self, map_obj, pos, vector):
        pass
