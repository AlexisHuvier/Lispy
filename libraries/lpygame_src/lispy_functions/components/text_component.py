from libraries.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpygame:components:text", ["str"])
def lpygame_components_text(args):
    return TextComponent(args[0])

@lispy_function("lpygame:components:text:text", ["TextComponent"])
def lpygame_components_text_text(args):
    return args[0].text

@lispy_function("lpygame:components:text:settext", ["TextComponent", "str"])
def lpygame_components_text_settext(args):
    args[0].text = args[1]
    args[0].update_render()

@lispy_function("lpygame:components:text:font", ["TextComponent"])
def lpygame_components_text_font(args):
    return args[0].font

@lispy_function("lpygame:components:text:setfont", ["TextComponent", "Font"])
def lpygame_components_text_setfont(args):
    args[0].font = args[1]
    args[0].update_render()

@lispy_function("lpygame:components:text:updaterender", ["TextComponent"])
def lpygame_components_text_updaterender(args):
    args[0].update_render()