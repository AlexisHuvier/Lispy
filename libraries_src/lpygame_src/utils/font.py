import pygame
from libraries_src.lpygame_src.utils.color import Color
from libraries_src.lpygame_src.utils.vec2 import Vec2

pygame.font.init()


class Font:
    def __init__(self, name="arial", size=16, bold=False, italic=False, underline=False, color=Color.from_name("BLACK"), background=None, antialias=False):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.color = color
        self.background = background
        self.antialias = antialias
        self.transformed_font = None
        self.update_font()

    def update_font(self):
        try:
            font = pygame.font.Font(self.name, self.size)
        except FileNotFoundError:
            font = pygame.font.SysFont(self.name, self.size)
        font.set_underline(self.underline)
        font.set_italic(self.italic)
        font.set_bold(self.bold)
        self.transformed_font = font

    def rendered_size(self, text):
        size = self.transformed_font.size(text)
        return Vec2(size[0], size[1])

    def render(self, text):
        if self.background:
            return self.transformed_font.render(text, self.antialias, self.color.get_rgba(), self.background.get_rgba())
        else:
            return self.transformed_font.render(text, self.antialias, self.color.get_rgba())

    def __eq__(self, other):
        return (isinstance(other, Font) and self.name == other.name and self.color == other.color and
                self.background == other.background and self.bold == other.bold and self.italic == other.italic and
                self.underline == other.underline and self.antialias == other.antialias)