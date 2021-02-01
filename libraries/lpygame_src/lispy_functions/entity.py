from libraries.lpygame_src import *
from lispy.error import lispy_function


@lispy_function("lpygame:entity")
def lpygame_entity(args):
    return Entity()

@lispy_function("lpygame:entity:addcomponent", ["Entity", "PositionComponent|ShowComponent|TextComponent"])
def lpygame_entity_addcomponent(args):
    return args[0].add_component(args[1])

@lispy_function("lpygame:entity:removecomponent", ["Entity", "str"])
def lpygame_entity_removecomponent(args):
    return args[0].remove_component(args[1])

@lispy_function("lpygame:entity:hascomponent", ["Entity", "str"])
def lpygame_entity_hascomponent(args):
    return args[0].has_component(args[1])

@lispy_function("lpygame:entity:getcomponent", ["Entity", "str"])
def lpygame_entity_getcomponent(args):
    return args[0].get_component(args[1])
