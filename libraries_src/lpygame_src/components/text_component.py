from libraries_src.lpygame_src.components.component import Component
from libraries_src.lpygame_src.utils import Font, Color


class TextComponent(Component):
    def __init__(self, text):
        super().__init__()
        self.font = Font("arial", 16, False, False, False, Color.from_name("BLACK"), None, False)
        self.text = text
        self.render = self.font.render(self.text)
    
    def update_render(self):
        self.render = self.font.render(self.text)