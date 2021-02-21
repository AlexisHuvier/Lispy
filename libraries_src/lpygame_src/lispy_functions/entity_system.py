from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.systems import *
from lispy.error import lispy_function


@lispy_function("lpg:es:add", ["EntitySystem", "Entity"], "Adding Entity to EntitySystem")
def lpg_es_add(args):
    return args[0].add_entity(args[1])

@lispy_function("lpg:es:remove", ["EntitySystem", "Entity"], "Remove Entity from EntitySystem")
def lpg_es_remove(args):
    return args[0].remove_entity(args[1])

@lispy_function("lpg:es:get", ["EntitySystem", "int"], "Getting Entity from EntitySystem by id")
def lpg_es_get(args):
    return args[0].get_entity(args[1])

@lispy_function("lpg:es:has", ["EntitySystem", "Entity"], "Return if EntitySystem has Entity")
def lpg_es_has(args):
    return args[0].has_entity(args[1])