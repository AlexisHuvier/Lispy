import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.identity = -1
        self.components = set()
        self.system = None
        self.image = None

    def add_component(self, component):
        component.entity = self
        self.components.add(component)
        return component

    def remove_component(self, component):
        for i in [i for i in self.components if isinstance(i, component)]:
            self.components.remove(i)

    def has_component(self, component):
        if len([c for c in self.components if isinstance(c, component)]):
            return True
        return False

    def get_component(self, component):
        liste = [i for i in self.components if isinstance(i, component)]
        try:
            return liste[0]
        except IndexError:
            pass

    def update(self):
        pass