from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function

@lispy_function("lpg:vec2:create", ["int|float", "int|float"], "Creating Vector2")
def lpg_vec2(args):
    return Vec2(args[0], args[1])

@lispy_function("lpg:vec2:setx", ["Vec2", "int|float"], "Setting x position to Vector2")
def lpg_vec2_setx(args):
    args[0].x = args[1]

@lispy_function("lpg:vec2:x", ["Vec2"], "Getting x position from Vector2")
def lpg_vec2_x(args):
    return args[0].x

@lispy_function("lpg:vec2:sety", ["Vec2", "int|float"], "Setting y position to Vector2")
def lpg_vec2_sety(args):
    args[0].y = args[1]

@lispy_function("lpg:vec2:y", ["Vec2"], "Getting y position from Vector2")
def lpg_vec2_y(args):
    return args[0].y

@lispy_function("lpg:vec2:setcoords", ["Vec2", "list"], "Setting coords to Vector2")
def lpg_vec2_setcoords(args):
    args[0].set_coords(args[0], args[1])

@lispy_function("lpg:vec2:coords", ["Vec2"], "Getting coords from Vector2")
def lpg_vec2_coords(args):
    return args[0].coords()

@lispy_function("lpg:vec2:normalized", ["Vec2"], "Getting normized Vector2")
def lpg_vec2_normalized(args):
    return args[0].normalized()

@lispy_function("lpg:vec2:zero", [], "Getting zero Vector2")
def lpg_vec2_zero(args):
    return Vec2.zero()

@lispy_function("lpg:vec2:one", [], "Getting one Vector2")
def lpg_vec2_one(args):
    return Vec2.one()