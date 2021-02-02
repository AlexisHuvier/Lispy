from libraries_src.lpygame_src import *
from lispy.error import lispy_function


@lispy_function("lpg:entity")
def lpg_entity(args):
    return Entity()

@lispy_function("lpg:entity:add", ["Entity", "PositionComponent|ShowComponent|TextComponent|SpriteComponent"])
def lpg_entity_add(args):
    return args[0].add_component(args[1])

@lispy_function("lpg:entity:remove", ["Entity", "str"])
def lpg_entity_remove(args):
    return args[0].remove_component(args[1])

@lispy_function("lpg:entity:has", ["Entity", "str"])
def lpg_entity_has(args):
    return args[0].has_component(args[1])

@lispy_function("lpg:entity:get", ["Entity", "str"])
def lpg_entity_get(args):
    return args[0].get_component(args[1])
