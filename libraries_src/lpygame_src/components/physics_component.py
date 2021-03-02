from libraries_src.lpygame_src.components.component import Component


class PhysicsComponent(Component):
    def __init__(self):
        super().__init__()
        self.gravity = 5
        self.max_gravity = self.gravity
        self.time_gravity = 5
        self.grounded = False
        self.time = self.time_gravity
        self.required_components.add("PositionComponent")

    def update(self):
        pos = self.entity.get_component("PositionComponent").pos()
        pos.y += self.gravity

        if self.entity.has_component("CollisionComponent"):
            if self.entity.get_component("CollisionComponent").can_go(pos, "GRAVITY"):
                self.grounded = False
                self.entity.get_component("PositionComponent").set_pos(pos)
            elif self.gravity > 0:
                self.grounded = True
                self.gravity = 2
            
            if self.time <= 0 and self.gravity < self.max_gravity and not self.grounded:
                self.gravity += 1
                self.time = self.time_gravity
            self.time -= 1
        else:
            self.entity.get_component("PositionComponent").set_pos(pos)