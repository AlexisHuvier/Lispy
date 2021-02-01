from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpygame:color")
def lpygame_color(args):
    return Color()

@lispy_function("lpygame:color:fromname", ["str"])
def lpygame_color_fromname(args):
    return Color.from_name(args[0])

@lispy_function("lpygame:color:fromhtml", ["str"])
def lpygame_color_fromhtml(args):
    return Color.from_html(args[0])

@lispy_function("lpygame:color:fromcolor", ["Color"])
def lpygame_color_fromcolor(args):
    return Color.from_color(args[0])

@lispy_function("lpygame:color:fromrgba", ["int|float", "int|float", "int|float", "int|float"])
def lpygame_color_fromrgba(args):
    return Color.from_rgba(args[0], args[1], args[2], args[3])

@lispy_function("lpygame:color:fromrgb", ["int|float", "int|float", "int|float"])
def lpygame_color_fromrgb(args):
    return Color.from_rgb(args[0], args[1], args[2])

@lispy_function("lpygame:color:gethtml", ["Color"])
def lpygame_color_gethtml(args):
    return args[0].get_html()

@lispy_function("lpygame:color:getrgba", ["Color"])
def lpygame_color_getrgba(args):
    return args[0].get_rgba()

@lispy_function("lpygame:color:getrgb", ["Color"])
def lpygame_color_getrgb(args):
    return args[0].get_rgb()

@lispy_function("lpygame:color:lighter", ["int|float"])
def lpygame_color_lighter(args):
    return args[0].lighter(args[0])

@lispy_function("lpygame:color:darker", ["int|float"])
def lpygame_color_darker(args):
    return args[0].darker(args[0])