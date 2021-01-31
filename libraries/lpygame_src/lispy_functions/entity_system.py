from libraries.lpygame_src import *
from libraries.lpygame_src.systems import *
from lispy.error import lispy_function


@lispy_function("lpygame:entitysystem:addentity", ["EntitySystem", "Entity"])
def lpygame_entitysystem_addentity(args):
    return args[0].add_entity(args[1])

@lispy_function("lpygame:entitysystem:removeentity", ["EntitySystem", "Entity"])
def lpygame_entitysystem_removeentity(args):
    return args[0].remove_entity(args[1])

@lispy_function("lpygame:entitysystem:getentity", ["EntitySystem", "int"])
def lpygame_entitysystem_getentity(args):
    return args[0].get_entity(args[1])

@lispy_function("lpygame:entitysystem:hasentity", ["EntitySystem", "Entity"])
def lpygame_entitysystem_hasentity(args):
    return args[0].has_entity(args[1])