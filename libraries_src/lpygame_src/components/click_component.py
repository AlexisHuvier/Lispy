from libraries_src.lpygame_src.components.component import Component


class ClickComponent(Component):
    def __init__(self, sprite):
        super().__init__()
        self.callback = None
        self.required_components.add("PositionComponent")
        if sprite:
            self.required_components.add("SpriteComponent")
        else:
            self.required_components.add("TextComponent")
        self.sprite = sprite
        
    def mousepress(self, evt):
        if self.callback is not None:
            pos = self.entity.get_component("PositionComponent").pos()
            if self.sprite:
                rect = self.entity.get_component("SpriteComponent").transformed_image.get_rect(x=pos.x, y=pos.y)
            else:
                rect = self.entity.get_component("TextComponent").render.get_rect(x=pos.x, y=pos.y)
            if rect.collidepoint(evt.pos):
                self.callback(self.entity, evt.pos)

        