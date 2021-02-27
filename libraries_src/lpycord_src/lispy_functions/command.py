from lispy.error import lispy_function
from libraries_src.lpycord_src import Command


@lispy_function("lpycord:command:create", ["str", "Procedure|NoneType"], "Creating a command with name and callback")
def lpycord_command_create(args):
    return Command(args[0], args[1])
    
@lispy_function("lpycord:command:name", ["Command"], "Getting command name")
def lpycord_command_name(args):
    return args[0].name

@lispy_function("lpycord:command:setname", ["Command", "str"], "Setting command name")
def lpycord_command_setname(args):
    args[0].name = args[1]

@lispy_function("lpycord:command:callback", ["Command"], "Getting command callback")
def lpycord_command_callback(args):
    return args[0].callback

@lispy_function("lpycord:command:setcallback", ["Command", "Procedure|NoneType"], "Setting command callback")
def lpycord_command_setcallback(args):
    args[0].callback = args[1]