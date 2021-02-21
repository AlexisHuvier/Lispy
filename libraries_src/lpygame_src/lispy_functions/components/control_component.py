from libraries_src.lpygame_src.components import *
from lispy.error import lispy_function


@lispy_function("lpg:comp:control:create", ["str"], "Creating ControlComponent by ControlType (FOURDIRECTION, UPDOWN, LEFTRIGHT)")
def lpg_comp_control(args):
    return ControlComponent(args[0])

@lispy_function("lpg:comp:control:speed", ["ControlComponent"], "Getting speed from ControlComponent")
def lpg_comp_control_speed(args):
    return args[0].speed

@lispy_function("lpy:comp:control:setspeed", ["ControlComponet", "int"], "Setting speed to ControlComponent")
def lpg_comp_control_setspeed(args):
    args[0].speed = args[1]

@lispy_function("lpg:comp:control:type", ["ControlComponent"], "Getting ControlType from ControlComponent")
def lpg_comp_control_type(args):
    return args[0].control_type

@lispy_function("lpy:comp:control:settype", ["ControlComponet", "str"], "Setting ControlType to ControlComponent (FOURDIRECTION, UPDOWN, LEFTRIGHT)")
def lpg_comp_control_settype(args):
    args[0].control_type = args[1]