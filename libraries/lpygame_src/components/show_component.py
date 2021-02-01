from libraries.lpygame_src.components.component import Component


class ShowComponent(Component):
    def __init__(self):
        super().__init__()
        self.required_components.add("PositionComponent")
        self.required_components.add("TextComponent")
    
    def show(self, screen):
        pos = self.entity.get_component("PositionComponent").pos()
        image = self.entity.get_component("TextComponent").render
        screen.blit(image, pos.coords())
    
    def show_debug(self, screen):
        pass