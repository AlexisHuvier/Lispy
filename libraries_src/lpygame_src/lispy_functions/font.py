from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpygame:font", ["str", "int", "bool", "bool", "bool", "Color", "Color|NoneType", "bool"])
def lpygame_font(args):
    return Font(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

@lispy_function("lpygame:font:rendersize", ["Font", "str"])
def lpygame_font_rendersize(args):
    return args[0].rendered_size(args[1])

@lispy_function("lpygame:font:name", ["Font"])
def lpygame_font_name(args):
    return args[0].name

@lispy_function("lpygame:font:setname", ["Font", "str"])
def lpygame_font_setname(args):
    args[0].name = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:size", ["Font"])
def lpygame_font_size(args):
    return args[0].size

@lispy_function("lpygame:font:setsize", ["Font", "int"])
def lpygame_font_setsize(args):
    args[0].size = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:bold", ["Font"])
def lpygame_font_bold(args):
    return args[0].bold

@lispy_function("lpygame:font:setbold", ["Font", "bool"])
def lpygame_font_setbold(args):
    args[0].bold = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:italic", ["Font"])
def lpygame_font_italic(args):
    return args[0].italic

@lispy_function("lpygame:font:setitalic", ["Font", "bool"])
def lpygame_font_setitalic(args):
    args[0].italic = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:underline", ["Font"])
def lpygame_font_underline(args):
    return args[0].underline

@lispy_function("lpygame:font:setunderline", ["Font", "bool"])
def lpygame_font_setunderline(args):
    args[0].underline = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:antialias", ["Font"])
def lpygame_font_antialias(args):
    return args[0].antialias

@lispy_function("lpygame:font:setantialias", ["Font", "bool"])
def lpygame_font_setantialias(args):
    args[0].antialias = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:color", ["Font"])
def lpygame_font_color(args):
    return args[0].color

@lispy_function("lpygame:font:setcolor", ["Font", "Color"])
def lpygame_font_setcolor(args):
    args[0].color = args[1]
    args[0].update_font()

@lispy_function("lpygame:font:background", ["Font"])
def lpygame_font_background(args):
    return args[0].background

@lispy_function("lpygame:font:setbackground", ["Font", "Color|NoneType"])
def lpygame_font_setbackground(args):
    args[0].background = args[1]
    args[0].update_font()
