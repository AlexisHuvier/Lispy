from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpg:color", [], "Creating basic Color")
def lpg_color(args):
    return Color()

@lispy_function("lpg:color:fromname", ["str"], "Creating Color from name")
def lpg_color_fromname(args):
    return Color.from_name(args[0])

@lispy_function("lpg:color:fromhtml", ["str"], "Creating Color from html")
def lpg_color_fromhtml(args):
    return Color.from_html(args[0])

@lispy_function("lpg:color:fromcolor", ["Color"], "Creating Color from other Color")
def lpg_color_fromcolor(args):
    return Color.from_color(args[0])

@lispy_function("lpg:color:fromrgba", ["int|float", "int|float", "int|float", "int|float"], "Creating Color from RGBA")
def lpg_color_fromrgba(args):
    return Color.from_rgba(args[0], args[1], args[2], args[3])

@lispy_function("lpg:color:fromrgb", ["int|float", "int|float", "int|float"], "Creating Color from RGB")
def lpg_color_fromrgb(args):
    return Color.from_rgb(args[0], args[1], args[2])

@lispy_function("lpg:color:gethtml", ["Color"], "Getting HTML from Color")
def lpg_color_gethtml(args):
    return args[0].get_html()

@lispy_function("lpg:color:getrgba", ["Color"], "Getting RGBA from Color")
def lpg_color_getrgba(args):
    return args[0].get_rgba()

@lispy_function("lpg:color:getrgb", ["Color"], "Getting RGB from Color")
def lpg_color_getrgb(args):
    return args[0].get_rgb()

@lispy_function("lpg:color:lighter", ["int|float"], "Getting lighter Color with force of lighting")
def lpg_color_lighter(args):
    return args[0].lighter(args[0])

@lispy_function("lpg:color:darker", ["int|float"], "Getting darker Color with force of darking")
def lpg_color_darker(args):
    return args[0].darker(args[0])