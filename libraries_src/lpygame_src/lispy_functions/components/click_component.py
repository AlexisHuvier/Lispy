from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:click:create", ["bool"], "Creating ClickComponent with bool to know if use sprite or text")
def lpg_comp_click(args):
    return ClickComponent(args[0])

@lispy_function("lpg:comp:click:callback", ["ClickComponent", "Procedure|NoneType"], "Setting component's callback")
def lpg_comp_click_callback(args):
    args[0].callback = args[1]