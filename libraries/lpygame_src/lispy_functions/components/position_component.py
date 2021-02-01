from libraries.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpygame:components:position", ["Vec2"])
def lpygame_components_position(args):
    return PositionComponent(args[0])

@lispy_function("lpygame:components:position:x", ["PositionComponent"])
def lpygame_components_position_x(args):
    return args[0].x

@lispy_function("lpygame:components:position:y", ["PositionComponent"])
def lpygame_components_position_y(args):
    return args[0].y

@lispy_function("lpygame:components:position:setx", ["PositionComponent", "int|float"])
def lpygame_components_position_setx(args):
    args[0].x = args[1]

@lispy_function("lpygame:components:position:sety", ["PositionComponent", "int|float"])
def lpygame_components_position_sety(args):
    args[0].y = args[1]

@lispy_function("lpygame:components:position:pos", ["PositionComponent"])
def lpygame_components_position_pos(args):
    return args[0].pos()

@lispy_function("lpygame:components:position:setpos", ["PositionComponent", "Vec2"])
def lpygame_components_position_setpos(args):
    args[0].set_pos(args[0])