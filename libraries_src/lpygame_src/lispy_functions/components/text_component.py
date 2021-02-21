from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:text", ["str"], "Creating TextComponent")
def lpg_comp_text(args):
    return TextComponent(args[0])

@lispy_function("lpg:comp:text:text", ["TextComponent"], "Getting text from TextComponent")
def lpg_comp_text_text(args):
    return args[0].text

@lispy_function("lpg:comp:text:settext", ["TextComponent", "str"], "Setting text to TextComponent")
def lpg_comp_text_settext(args):
    args[0].text = args[1]
    args[0].update_render()

@lispy_function("lpg:comp:text:font", ["TextComponent"], "Getting font from TextComponent")
def lpg_comp_text_font(args):
    return args[0].font

@lispy_function("lpg:comp:text:setfont", ["TextComponent", "Font"], "Setting font to TextComponent")
def lpg_comp_text_setfont(args):
    args[0].font = args[1]
    args[0].update_render()

@lispy_function("lpg:comp:text:update", ["TextComponent"], "Update render of TextComponent")
def lpg_comp_text_update(args):
    args[0].update_render()