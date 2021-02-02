from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpg:font", ["str", "int", "bool", "bool", "bool", "Color", "Color|NoneType", "bool"])
def lpg_font(args):
    return Font(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

@lispy_function("lpg:font:rendersize", ["Font", "str"])
def lpg_font_rendersize(args):
    return args[0].rendered_size(args[1])

@lispy_function("lpg:font:name", ["Font"])
def lpg_font_name(args):
    return args[0].name

@lispy_function("lpg:font:setname", ["Font", "str"])
def lpg_font_setname(args):
    args[0].name = args[1]
    args[0].update_font()

@lispy_function("lpg:font:size", ["Font"])
def lpg_font_size(args):
    return args[0].size

@lispy_function("lpg:font:setsize", ["Font", "int"])
def lpg_font_setsize(args):
    args[0].size = args[1]
    args[0].update_font()

@lispy_function("lpg:font:bold", ["Font"])
def lpg_font_bold(args):
    return args[0].bold

@lispy_function("lpg:font:setbold", ["Font", "bool"])
def lpg_font_setbold(args):
    args[0].bold = args[1]
    args[0].update_font()

@lispy_function("lpg:font:italic", ["Font"])
def lpg_font_italic(args):
    return args[0].italic

@lispy_function("lpg:font:setitalic", ["Font", "bool"])
def lpg_font_setitalic(args):
    args[0].italic = args[1]
    args[0].update_font()

@lispy_function("lpg:font:underline", ["Font"])
def lpg_font_underline(args):
    return args[0].underline

@lispy_function("lpg:font:setunderline", ["Font", "bool"])
def lpg_font_setunderline(args):
    args[0].underline = args[1]
    args[0].update_font()

@lispy_function("lpg:font:antialias", ["Font"])
def lpg_font_antialias(args):
    return args[0].antialias

@lispy_function("lpg:font:setantialias", ["Font", "bool"])
def lpg_font_setantialias(args):
    args[0].antialias = args[1]
    args[0].update_font()

@lispy_function("lpg:font:color", ["Font"])
def lpg_font_color(args):
    return args[0].color

@lispy_function("lpg:font:setcolor", ["Font", "Color"])
def lpg_font_setcolor(args):
    args[0].color = args[1]
    args[0].update_font()

@lispy_function("lpg:font:background", ["Font"])
def lpg_font_background(args):
    return args[0].background

@lispy_function("lpg:font:setbackground", ["Font", "Color|NoneType"])
def lpg_font_setbackground(args):
    args[0].background = args[1]
    args[0].update_font()
