import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        super(Entity, self).__init__()
        self.identity = -1
        self.components = set()
        self.system = None
        self.image = None

    def add_component(self, component):
        if isinstance(component, tuple(type(c) for c in self.components)):
            return "Entity already have a " + str(component.__class__.__name__)
        else:
            for i in component.required_components:
                if i not in set(c.__class__.__name__ for c in self.components):
                    return str(component.__class__.__name__) + " require " + str(i.__name__)
            for i in component.incompatible_components:
                if i in set(c.__class__.__name__ for c in self.components):
                    return str(component.__class__.__name__) + " is incompatible with " + str(i.__name__)
        component.entity = self
        self.components.add(component)
        return component

    def remove_component(self, component):
        for i in [i for i in self.components if i.__class__.__name__ == component]:
            self.components.remove(i)

    def has_component(self, component):
        if len([i for i in self.components if i.__class__.__name__ == component]):
            return True
        return False

    def get_component(self, component):
        liste = [i for i in self.components if i.__class__.__name__ == component]
        try:
            return liste[0]
        except IndexError:
            pass

    def update(self):
        pass

    def event(self, evt):
        pass