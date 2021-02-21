from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:position:create", ["Vec2"], "Creating PositionComponent")
def lpg_comp_position(args):
    return PositionComponent(args[0])

@lispy_function("lpg:comp:position:x", ["PositionComponent"], "Getting x position from PositionComponent")
def lpg_comp_position_x(args):
    return args[0].x

@lispy_function("lpg:comp:position:y", ["PositionComponent"], "Getting y position from PositionComponent")
def lpg_comp_position_y(args):
    return args[0].y

@lispy_function("lpg:comp:position:setx", ["PositionComponent", "int|float"], "Setting x position to PositionComponent")
def lpg_comp_position_setx(args):
    args[0].x = args[1]

@lispy_function("lpg:comp:position:sety", ["PositionComponent", "int|float"], "Setting y position to PositionComponent")
def lpg_comp_position_sety(args):
    args[0].y = args[1]

@lispy_function("lpg:comp:position:pos", ["PositionComponent"], "Getting position from PositionComponent")
def lpg_comp_position_pos(args):
    return args[0].pos()

@lispy_function("lpg:comp:position:setpos", ["PositionComponent", "Vec2"], "Setting position from PositionComponent")
def lpg_comp_position_setpos(args):
    args[0].set_pos(args[0])