from libraries_src.lpygame_src.components.component import Component


class CollisionComponent(Component):
    def __init__(self):
        super().__init__()
        self.required_components.add("PositionComponent")
        self.required_components.add("SpriteComponent")
        self.solid = True
        self.callback = None
    
    def can_go(self, pos, cause="UNKNOWN"):
        rect = self.entity.get_component("SpriteComponent").transformed_image.get_rect(x=pos.x, y=pos.y)
        for entity in self.entity.system.entities:
            if entity != self.entity and entity.has_component("SpriteComponent") and entity.has_component("PositionComponent") and entity.has_component("CollisionComponent"):
                position = entity.get_component("PositionComponent").pos()
                other_rect = entity.get_component("SpriteComponent").transformed_image.get_rect(x=position.x, y=position.y)
                if rect.colliderect(other_rect):
                    if self.callback:
                        self.callback(entity, cause)
                    
                    if entity.get_component("CollisionComponent").solid and self.solid:
                        return False
        return True