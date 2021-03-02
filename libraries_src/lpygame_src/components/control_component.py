from libraries_src.lpygame_src.components.component import Component

import pygame.locals as const


class ControlComponent(Component):
    def __init__(self, control_type):
        super().__init__()
        self.control_type = control_type
        self.speed = 5

        self.controls = {
            "UP": const.K_UP,
            "LEFT": const.K_LEFT,
            "RIGHT": const.K_RIGHT,
            "DOWN": const.K_DOWN,
            "JUMP": const.K_UP
        }

        self.keypressed = set()
        self.required_components.add("PositionComponent")
        self.jumping = False
        if control_type == "CLASSICJUMP":
            self.required_components.add("PhysicsComponent")
        
    def update(self):
        for i in self.keypressed:
            self.move(i)

    def move(self, key):
        pos = self.entity.get_component("PositionComponent").pos()
        cause = "UNKNOWN"
        if key == self.controls["UP"]:
            if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                pos.y -= self.speed
                cause = "UPCONTROL"
            elif self.control_type == "CLASSICJUMP":
                phys = self.entity.get_component("PhysicsComponent")
                if phys.grounded and not self.jumping:
                    phys.grounded = False
                    self.jumping = True
                    phys.gravity = -phys.max_gravity


        elif key == self.controls["DOWN"]:
            if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                pos.y += self.speed
                cause = "DOWNCONTROL"
        
        elif key == self.controls["LEFT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                pos.x -= self.speed
                cause = "LEFTCONTROL"
        
        elif key == self.controls["RIGHT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT", "CLASSICJUMP"):
                pos.x += self.speed
                cause = "RIGHTCONTROL"
        
        if pos != self.entity.get_component("PositionComponent").pos():
            if self.entity.has_component("CollisionComponent"):
                if self.entity.get_component("CollisionComponent").can_go(pos, cause):
                    self.entity.get_component("PositionComponent").set_pos(pos)
            else:
                self.entity.get_component("PositionComponent").set_pos(pos)
        
    def keyup(self, evt):
        if evt.key in self.keypressed:
            self.keypressed.remove(evt.key)
        if self.control_type == "CLASSICJUMP" and evt.key == self.controls["UP"]:
            self.jumping = False
    
    def keypress(self, evt):
        if evt.key not in self.keypressed:
            self.keypressed.add(evt.key)