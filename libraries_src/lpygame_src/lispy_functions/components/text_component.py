from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:text", ["str"])
def lpg_comp_text(args):
    return TextComponent(args[0])

@lispy_function("lpg:comp:text:text", ["TextComponent"])
def lpg_comp_text_text(args):
    return args[0].text

@lispy_function("lpg:comp:text:settext", ["TextComponent", "str"])
def lpg_comp_text_settext(args):
    args[0].text = args[1]
    args[0].update_render()

@lispy_function("lpg:comp:text:font", ["TextComponent"])
def lpg_comp_text_font(args):
    return args[0].font

@lispy_function("lpg:comp:text:setfont", ["TextComponent", "Font"])
def lpg_comp_text_setfont(args):
    args[0].font = args[1]
    args[0].update_render()

@lispy_function("lpg:comp:text:update", ["TextComponent"])
def lpg_comp_text_update(args):
    args[0].update_render()