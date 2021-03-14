from libraries_src.lpygame_src.components.component import Component
import pygame.locals as const


class MoveComponent(Component):
    def __init__(self, to_pos):
        super().__init__()
        self.to_pos = to_pos
        self.speed = 5
        self.required_components.add("PositionComponent")
        
    def update(self):
        pos = self.entity.get_component("PositionComponent").pos()
        if self.to_pos.x < pos.x:
            pos.x -= self.speed
        elif self.to_pos.x > pos.x:
            pos.x += self.speed
        if self.to_pos.y < pos.y:
            pos.y -= self.speed
        elif self.to_pos.y > pos.y:
            pos.y += self.speed
            
        if self.entity.has_component("CollisionComponent"):
            if self.entity.get_component("CollisionComponent").can_go(pos, "MOVE"):
                self.entity.get_component("PositionComponent").set_pos(pos)
        else:
            self.entity.get_component("PositionComponent").set_pos(pos)
