from libraries.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpygame:components:show")
def lpygame_components_show(args):
    return ShowComponent()