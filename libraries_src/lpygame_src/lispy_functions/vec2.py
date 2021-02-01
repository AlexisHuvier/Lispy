from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function

@lispy_function("lpygame:vec2", ["int|float", "int|float"])
def lpygame_vec2(args):
    return Vec2(args[0], args[1])

@lispy_function("lpygame:vec2:setx", ["Vec2", "int|float"])
def lpygame_vec2_setx(args):
    args[0].x = args[1]

@lispy_function("lpygame:vec2:x", ["Vec2"])
def lpygame_vec2_x(args):
    return args[0].x

@lispy_function("lpygame:vec2:sety", ["Vec2"])
def lpygame_vec2_sety(args):
    args[0].y = args[1]

@lispy_function("lpygame:vec2:y", ["Vec2", "int|float"])
def lpygame_vec2_y(args):
    return args[0].y

@lispy_function("lpygame:vec2:setcoords", ["Vec2", "list"])
def lpygame_vec2_setcoords(args):
    args[0].set_coords(args[0], args[1])

@lispy_function("lpygame:vec2:coords", ["Vec2"])
def lpygame_vec2_coords(args):
    return args[0].coords()

@lispy_function("lpygame:vec2:normalized", ["Vec2"])
def lpygame_vec2_normalized(args):
    return args[0].normalized()

@lispy_function("lpygame:vec2:zero")
def lpygame_vec2_zero(args):
    return Vec2.zero()

@lispy_function("lpygame:vec2:one")
def lpygame_vec2_one(args):
    return Vec2.one()