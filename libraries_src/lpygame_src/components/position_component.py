from libraries_src.lpygame_src.components.component import Component
from libraries_src.lpygame_src.utils import Vec2


class PositionComponent(Component):
    def __init__(self, vector):
        super().__init__()
        self.x = vector.x
        self.y = vector.y
    
    def pos(self):
        return Vec2(self.x, self.y)
    
    def set_pos(self, vector):
        self.x = vector.x
        self.y = vector.y