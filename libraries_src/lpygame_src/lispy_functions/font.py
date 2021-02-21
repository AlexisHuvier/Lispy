from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpg:font:create", ["str", "int", "bool", "bool", "bool", "Color", "Color|NoneType", "bool"], "Create Font by name, size, bold, italic, underline, color, background and antialias")
def lpg_font(args):
    return Font(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])

@lispy_function("lpg:font:rendersize", ["Font", "str"], "Getting rendersize of text by Font")
def lpg_font_rendersize(args):
    return args[0].rendered_size(args[1])

@lispy_function("lpg:font:name", ["Font"], "Getting name from Font")
def lpg_font_name(args):
    return args[0].name

@lispy_function("lpg:font:setname", ["Font", "str"], "Setting name to Font")
def lpg_font_setname(args):
    args[0].name = args[1]
    args[0].update_font()

@lispy_function("lpg:font:size", ["Font"], "Getting size from Font")
def lpg_font_size(args):
    return args[0].size

@lispy_function("lpg:font:setsize", ["Font", "int"], "Setting size to Font")
def lpg_font_setsize(args):
    args[0].size = args[1]
    args[0].update_font()

@lispy_function("lpg:font:bold", ["Font"], "Return if font is bold")
def lpg_font_bold(args):
    return args[0].bold

@lispy_function("lpg:font:setbold", ["Font", "bool"], "Setting if font is bold")
def lpg_font_setbold(args):
    args[0].bold = args[1]
    args[0].update_font()

@lispy_function("lpg:font:italic", ["Font"], "Return if font is italic")
def lpg_font_italic(args):
    return args[0].italic

@lispy_function("lpg:font:setitalic", ["Font", "bool"], "Setting if font is italic")
def lpg_font_setitalic(args):
    args[0].italic = args[1]
    args[0].update_font()

@lispy_function("lpg:font:underline", ["Font"], "Return if font is underline")
def lpg_font_underline(args):
    return args[0].underline

@lispy_function("lpg:font:setunderline", ["Font", "bool"], "Setting if font is underline")
def lpg_font_setunderline(args):
    args[0].underline = args[1]
    args[0].update_font()

@lispy_function("lpg:font:antialias", ["Font"], "Return if font has antialiasing")
def lpg_font_antialias(args):
    return args[0].antialias

@lispy_function("lpg:font:setantialias", ["Font", "bool"], "Setting if font has antialiasing")
def lpg_font_setantialias(args):
    args[0].antialias = args[1]
    args[0].update_font()

@lispy_function("lpg:font:color", ["Font"], "Getting Color from Font")
def lpg_font_color(args):
    return args[0].color

@lispy_function("lpg:font:setcolor", ["Font", "Color"], "Setting Color to Font")
def lpg_font_setcolor(args):
    args[0].color = args[1]
    args[0].update_font()

@lispy_function("lpg:font:background", ["Font"], "Getting background from Font")
def lpg_font_background(args):
    return args[0].background

@lispy_function("lpg:font:setbackground", ["Font", "Color|NoneType"], "Setting background to Font")
def lpg_font_setbackground(args):
    args[0].background = args[1]
    args[0].update_font()
