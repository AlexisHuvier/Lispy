from libraries.lpygame_src import *
from libraries.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpygame:font", ["str", "int", "bool", "bool", "bool", "Color", "Color|NoneType", "bool"])
def lpygame_font(args):
    return Font(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

@lispy_function("lpygame:font:rendersize", ["Font", "str"])
def lpygame_font_rendersize(args):
    return args[0].rendered_size(args[1])