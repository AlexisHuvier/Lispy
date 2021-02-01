import pygame
from libraries.lpygame_src.utils import Font, Color


class EntitySystem:
    def __init__(self, world):
        self.world = world
        self.entities = []
        self.debugfont = Font("arial", 15, False, False, False, Color.from_name("RED"), None, False)

    def get_entity(self, identity):
        for i in self.entities:
            if i.identity == identity:
                return i

    def add_entity(self, entity):
        if len(self.entities):
            entity.identity = self.entities[-1].identity + 1
        else:
            entity.identity = 0
        self.entities.append(entity)
        entity.system = self
        return entity

    def has_entity(self, entity):
        return entity in self.entities

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
        else:
            return "Entity has not in EntitySystem"

    def update(self):
        for i in self.entities:
            i.update()

    def keypress(self, evt):
        pass

    def keyup(self, evt):
        pass

    def mousepress(self, evt):
        pass

    def mousemotion(self, evt):
        pass

    def show(self):
        for i in self.entities:
            if i.has_component("ShowComponent"):
                i.get_component("ShowComponent").show(self.world.window.screen)

    def show_debug(self):
        for i in self.entities:
            if i.has_component("PositionComponent"):
                pos = i.get_component("PositionComponent").pos()
                render = self.debugfont.render("ID : "+str(i.identity))
                self.world.window.screen.blit(render, (pos.x, pos.y - 20))
            if i.has_component("ShowComponent"):
                i.get_component("ShowComponent").show(self.world.window.screen)