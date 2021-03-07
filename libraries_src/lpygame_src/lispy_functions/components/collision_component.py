from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:collision:create", [], "Creating CollisionComponent")
def lpg_comp_collision(args):
    return CollisionComponent()

@lispy_function("lpg:comp:collision:solid", ["CollisionComponent"], "Return if entity is solid")
def lpg_comp_collision_solid(args):
    return args[0].solid

@lispy_function("lpg:comp:collision:setsolid", ["CollisionComponent", "bool"], "Setting if entity is solid")
def lpg_comp_collision_setsolid(args):
    args[0].solid = args[1]

@lispy_function("lpg:comp:collision:callback", ["CollisionComponent"], "Getting collision callback")
def lpg_comp_collision_callback(args):
    return args[0].callback

@lispy_function("lpg:comp:collision:setcallback", ["CollisionComponent", "Procedure"], "Setting collision callback with entity, other entity and cause as args")
def lpg_comp_collision_setcallback(args):
    args[0].callback = args[1]

@lispy_function("lpg:comp:collision:cango", ["CollisionComponent", "Vec2", "str"], "Returning if entity can go to position with a cause if it collide")
def lpg_comp_collision_cango(args):
    return args[0].can_go(args[1], args[2])