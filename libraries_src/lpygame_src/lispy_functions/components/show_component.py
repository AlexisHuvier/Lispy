from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:show", ["bool"])
def lpg_comp_show(args):
    return ShowComponent(args[0])