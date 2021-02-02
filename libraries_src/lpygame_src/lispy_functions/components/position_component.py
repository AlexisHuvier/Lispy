from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:position", ["Vec2"])
def lpg_comp_position(args):
    return PositionComponent(args[0])

@lispy_function("lpg:comp:position:x", ["PositionComponent"])
def lpg_comp_position_x(args):
    return args[0].x

@lispy_function("lpg:comp:position:y", ["PositionComponent"])
def lpg_comp_position_y(args):
    return args[0].y

@lispy_function("lpg:comp:position:setx", ["PositionComponent", "int|float"])
def lpg_comp_position_setx(args):
    args[0].x = args[1]

@lispy_function("lpg:comp:position:sety", ["PositionComponent", "int|float"])
def lpg_comp_position_sety(args):
    args[0].y = args[1]

@lispy_function("lpg:comp:position:pos", ["PositionComponent"])
def lpg_comp_position_pos(args):
    return args[0].pos()

@lispy_function("lpg:comp:position:setpos", ["PositionComponent", "Vec2"])
def lpg_comp_position_setpos(args):
    args[0].set_pos(args[0])