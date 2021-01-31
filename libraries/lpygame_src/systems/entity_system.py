import pygame
from libraries.lpygame_src.utils import Font, Color


class EntitySystem:
    def __init__(self, world):
        self.world = world
        self.entities = pygame.sprite.Group()
        self.debugfont = Font("arial", 15, False, False, False, Color.from_name("RED"), None, False)

    def get_entity(self, identity):
        for i in self.entities:
            if i.identity == identity:
                return i

    def add_entity(self, entity):
        if len(self.entities):
            entity.identity = self.entities.sprites()[-1].identity + 1
        else:
            entity.identity = 0
        self.entities.add(entity)
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
        self.entities.draw(self.world.window.screen)

    def show_debug(self):
        for i in self.entities.sprites():
            render = self.debugfont.render("ID : "+str(i.identity))
            self.world.window.blit(render, (i.rect.x + i.rect.width / 2 - render.get_width()/2, i.rect.y - 20))