from libraries.lpygame_src import *
from libraries.lpygame_src.utils import *
from lispy.error import lispy_function
import math


@lispy_function("lpygame:win", ["str", "Vec2"])
def lpygame_win(args):
    return Window(args[0], args[1])

@lispy_function("lpygame:win:run", ["Window"])
def lpygame_win_run(args):
    args[0].run()

@lispy_function("lpygame:win:setdebug", ["Window", "bool"])
def lpygame_win_setdebug(args):
    args[0].debug = args[1]

@lispy_function("lpygame:win:debug", ["Window"])
def lpygame_win_debug(args):
    return args[0].debug

@lispy_function("lpygame:win:setcolor", ["Window", "Color"])
def lpygame_win_setcolor(args):
    args[0].color = args[1]

@lispy_function("lpygame:win:color", ["Window"])
def lpygame_win_color(args):
    return args[0].color

@lispy_function("lpygame:win:fps", ["Window"])
def lpygame_win_fps(args):
    try:
        return round(args[0].clock.get_fps())
    except:
        return math.inf

@lispy_function("lpygame:win:setfps", ["Window", "int"])
def lpygame_win_setfps(args):
    args[0].fps = args[1]

@lispy_function("lpygame:win:world", ["Window"])
def lpygame_win_world(args):
    return args[0].world

@lispy_function("lpygame:win:setworld", ["Window", "World"])
def lpygame_win_setworld(args):
    args[0].world = args[1]