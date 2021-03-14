from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:move:create", ["Vec2"], "Creating MoveComponent by destination position")
def lpg_comp_move(args):
    return MoveComponent(args[0])

@lispy_function("lpg:comp:move:speed", ["MoveComponent"], "Getting speed from MoveComponent")
def lpg_comp_move_speed(args):
    return args[0].speed

@lispy_function("lpg:comp:move:setspeed", ["MoveComponent", "int"], "Setting speed to MoveComponent")
def lpg_comp_move_setspeed(args):
    args[0].speed = args[1]

@lispy_function("lpg:comp:move:pos", ["MoveComponent"], "Getting destination position from MoveComponent")
def lpg_comp_move_pos(args):
    return args[0].to_pos

@lispy_function("lpg:comp:move:setpos", ["MoveComponent", "Vec2"], "Setting destination position to MoveComponent")
def lpg_comp_move_setpos(args):
    args[0].to_pos = args[1]