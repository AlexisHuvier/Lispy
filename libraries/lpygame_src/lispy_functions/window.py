from libraries.lpygame_src import *
from libraries.lpygame_src.utils import *
from lispy.error import lispy_function


@lispy_function("lpygame:win", ["str", "Vec2", "Color"])
def lpygame_win(args):
    return Window(args[0], args[1], args[2])

@lispy_function("lpygame:win:run", ["Window"])
def lpygame_win_run(args):
    args[0].run()

@lispy_function("lpygame:win:setdebug", ["Window", "bool"])
def lpygame_win_setdebug(args):
    args[0].debug = args[1]

@lispy_function("lpygame:win:debug", ["Window"])
def lpygame_win_debug(args):
    return args[0].debug