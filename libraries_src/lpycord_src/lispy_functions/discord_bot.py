from lispy.error import lispy_function
from libraries_src.lpycord_src import Bot


@lispy_function("lpycord:bot:create", ["str"], "Creating a bot with prefix")
def lpycord_bot_create(args):
    return Bot(args[0])

@lispy_function("lpycord:bot:addcommand", ["Bot", "Command"], "Adding command to bot")
def lpycord_bot_addcommand(args):
    args[0].commands.append(args[1])

@lispy_function("lpycord:bot:removecommand", ["Bot", "Command"], "Remove command from bot")
def lpycord_bot_removecommand(args):
    args[0].commands.remove(args[1])

@lispy_function("lpycord:bot:commands", ["Bot"], "Listing commands")
def lpycord_bot_commands(args):
    return args[0].commands

@lispy_function("lpycord:bot:prefix", ["Bot"], "Getting bot prefix")
def lpycord_bot_prefix(args):
    return args[0].prefix

@lispy_function("lpycord:bot:setprefix", ["Bot", "str"], "Setting bot prefix")
def lpycord_bot_setprefix(args):
    args[0].prefix = args[1]

@lispy_function("lpycord:bot:run", ["Bot", "str"], "Launching bot with token")
def lpycord_bot_run(args):
    args[0].run(args[1])