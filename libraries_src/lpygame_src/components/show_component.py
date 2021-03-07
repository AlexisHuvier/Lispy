from libraries_src.lpygame_src.components.component import Component


class ShowComponent(Component):
    def __init__(self, sprite):
        super().__init__()
        self.required_components.add("PositionComponent")
        if sprite:
            self.required_components.add("SpriteComponent")
        else:
            self.required_components.add("TextComponent")
        self.sprite = sprite
        self.displayed = True
    
    def show(self, screen):
        if self.displayed:
            pos = self.entity.get_component("PositionComponent").pos()
            if self.sprite:
                image = self.entity.get_component("SpriteComponent").transformed_image
            else:
                image = self.entity.get_component("TextComponent").render
            screen.blit(image, pos.coords())
    
    def show_debug(self, screen):
        pass