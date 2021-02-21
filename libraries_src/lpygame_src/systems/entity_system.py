import pygame


class EntitySystem:
    def __init__(self, world):
        self.world = world
        self.entities = []

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

    def event(self, evt):
        for i in self.entities:
            i.event(evt)

    def update(self):
        for i in self.entities:
            i.update()

    def keypress(self, evt):
        for i in self.entities:
            i.keypress(evt)

    def keyup(self, evt):
        for i in self.entities:
            i.keyup(evt)

    def mousepress(self, evt):
        for i in self.entities:
            i.mousepress(evt)

    def mousemotion(self, evt):
        for i in self.entities:
            i.mousemotion(evt)

    def show(self):
        for i in self.entities:
            i.show(self.world.window.screen)

    def show_debug(self):
        for i in self.entities:
            i.show_debug(self.world.window.screen)