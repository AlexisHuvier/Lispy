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
        
    def update(self):
        for i in self.keypressed:
            self.move(i)

    def move(self, key):
        pos = self.entity.get_component("PositionComponent").pos()
        if key == self.controls["UP"]:
            if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                pos.y -= self.speed

        elif key == self.controls["DOWN"]:
            if self.control_type in ("FOURDIRECTION", "UPDOWN"):
                pos.y += self.speed
        
        elif key == self.controls["LEFT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT"):
                pos.x -= self.speed
        
        elif key == self.controls["RIGHT"]:
            if self.control_type in ("FOURDIRECTION", "LEFTRIGHT"):
                pos.x += self.speed
        
        if pos != self.entity.get_component("PositionComponent").pos():
            self.entity.get_component("PositionComponent").set_pos(pos)
        
    def keyup(self, evt):
        if evt.key in self.keypressed:
            self.keypressed.remove(evt.key)
    
    def keypress(self, evt):
        if evt.key not in self.keypressed:
            self.keypressed.add(evt.key)