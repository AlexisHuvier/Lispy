from libraries.lpygame_src import *
from lispy.error import lispy_function


@lispy_function("lpygame:entity")
def lpygame_entity(args):
    return Entity()
