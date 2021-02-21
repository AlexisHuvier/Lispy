from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpg:world:create", ["Window"], "Creating World from Window")
def lpg_world(args):
    return World(args[0])

@lispy_function("lpg:world:getsystem", ["World", "str"], "Getting system from Window by its name")
def lpg_world_getsystem(args):
    return args[0].get_system(args[1])