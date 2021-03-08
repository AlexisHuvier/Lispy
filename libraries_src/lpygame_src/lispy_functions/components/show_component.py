from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:show:create", ["bool"], "Creating ShowComponent with bool to know if use sprite or text")
def lpg_comp_show(args):
    return ShowComponent(args[0])

@lispy_function("lpg:comp:show:displayed", ["ShowComponent"], "Getting if entity will be displayed")
def lpg_comp_show_displayed(args):
    return args[0].displayed

@lispy_function("lpg:comp:show:setdisplayed", ["ShowComponent", "bool"], "Setting if entity will be displayed")
def lpg_comp_show_setdisplayed(args):
    args[0].displayed = args[1]