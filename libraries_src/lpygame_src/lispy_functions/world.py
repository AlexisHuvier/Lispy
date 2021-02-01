from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpygame:world", ["Window"])
def lpygame_world(args):
    return World(args[0])

@lispy_function("lpygame:world:getsystem", ["World", "str"])
def lpygame_world_getsystem(args):
    return args[0].get_system(args[1])