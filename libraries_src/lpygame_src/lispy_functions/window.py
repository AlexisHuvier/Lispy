from libraries_src.lpygame_src import *
from libraries_src.lpygame_src.utils import *
from lispy.error import lispy_function
import math


@lispy_function("lpg:win", ["str", "Vec2"], "Creating Window from name and Vector2")
def lpg_win(args):
    return Window(args[0], args[1])

@lispy_function("lpg:win:run", ["Window"], "Running Window")
def lpg_win_run(args):
    args[0].run()

@lispy_function("lpg:win:setdebug", ["Window", "bool"], "Setting if window is debug")
def lpg_win_setdebug(args):
    args[0].debug = args[1]

@lispy_function("lpg:win:debug", ["Window"], "Getting if window is debug")
def lpg_win_debug(args):
    return args[0].debug

@lispy_function("lpg:win:setcolor", ["Window", "Color"], "Setting Color to Window")
def lpg_win_setcolor(args):
    args[0].color = args[1]

@lispy_function("lpg:win:color", ["Window"], "Getting Color from Window")
def lpg_win_color(args):
    return args[0].color

@lispy_function("lpg:win:fps", ["Window"], "Getting FPS from Window")
def lpg_win_fps(args):
    try:
        return round(args[0].clock.get_fps())
    except:
        return math.inf

@lispy_function("lpg:win:setfps", ["Window", "int"], "Setting FPS limiter to Window")
def lpg_win_setfps(args):
    args[0].fps = args[1]

@lispy_function("lpg:win:world", ["Window"], "Getting World from Window")
def lpg_win_world(args):
    return args[0].world

@lispy_function("lpg:win:setworld", ["Window", "World"], "Setting World to Window")
def lpg_win_setworld(args):
    args[0].world = args[1]