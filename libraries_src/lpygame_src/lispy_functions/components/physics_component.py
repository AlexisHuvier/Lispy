from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:physics:create", [], "Creating PhysicsComponent")
def lpg_comp_physics(args):
    return PhysicsComponent()

@lispy_function("lpg:comp:physics:gravity", ["PhysicsComponent"], "Getting current gravity")
def lpg_comp_physics_gravity(args):
    return args[0].gravity

@lispy_function("lpg:comp:physics:setgravity", ["PhysicsComponent", "int"], "Setting current gravity")
def lpg_comp_physics_setgravity(args):
    args[0].gravity = args[1]

@lispy_function("lpg:comp:physics:maxgravity", ["PhysicsComponent"], "Getting current max gravity")
def lpg_comp_physics_maxgravity(args):
    return args[0].max_gravity

@lispy_function("lpg:comp:physics:setmaxgravity", ["PhysicsComponent", "int"], "Setting current max gravity")
def lpg_comp_physics_setmaxgravity(args):
    args[0].max_gravity = args[1]