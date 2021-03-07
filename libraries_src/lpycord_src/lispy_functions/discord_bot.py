from lispy.error import lispy_function
from libraries_src.lpycord_src import Bot


@lispy_function("lpycord:bot:create", ["str"], "Creating a bot with prefix")
def lpycord_bot_create(args):
    return Bot(args[0])

@lispy_function("lpycord:bot:latency", ["Bot"], "Measuring latency between a HEARTBEAT and a HEARTBEAT_ACK in seconds")
def lpycord_bot_latency(args):
    return args[0].latency

@lispy_function("lpycord:bot:user", ["Bot"], "Getting user of bot (if connected or None)")
def lpycord_bot_user(args):
    return args[0].user

@lispy_function("lpycord:bot:guilds", ["Bot"], "Getting guilds of Bot")
def lpycord_bot_guilds(args):
    return args[0].guilds

@lispy_function("lpycord:bot:isready", ["Bot"], "Returning if bot's cache is ready")
def lpycord_bot_isready(args):
    return args[0].is_ready()

@lispy_function("lpycord:bot:close", ["Bot"], "Closing Bot")
def lpycord_bot_close(args):
    args[0].close()

@lispy_function("lpycord:bot:getchannel", ["Bot", "int"], "Getting a channel by id")
def lpycord_bot_getchannel(args):
    return args[0].get_channel(args[1])

@lispy_function("lpycord:bot:getguild", ["Bot", "int"], "Getting a guild by id")
def lpycord_bot_getguild(args):
    return args[0].get_guild(args[1])

@lispy_function("lpycord:bot:getuser", ["Bot", "int"], "Getting a user by id")
def lpycord_bot_getuser(args):
    return args[0].get_user(args[1])

@lispy_function("lpycord:bot:getemoji", ["Bot", "int"], "Getting a emoji by id")
def lpycord_bot_getemoji(args):
    return args[0].get_emoji(args[1])

@lispy_function("lpycord:bot:users", ["Bot"], "Getting users of Bot")
def lpycord_bot_users(args):
    return args[0].users

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

@lispy_function("lpycord:bot:setready", ["Bot", "Procedure|NoneType"], "Setting Function called when bot is ready (or None)")
def lpycord_bot_setready(args):
    args[0].callbacks["ready"] = args[1]

@lispy_function("lpycord:bot:setmessage", ["Bot", "Procedure|NoneType"], "Setting Function called when bot recieve a message (or None)")
def lpycord_bot_setmessage(args):
    args[0].callbacks["message"] = args[1]

@lispy_function("lpycord:bot:setmessagedelete", ["Bot", "Procedure|NoneType"], "Setting Function called when a message is deleted (or None)")
def lpycord_bot_setmessagedelete(args):
    args[0].callbacks["message_delete"] = args[1]

@lispy_function("lpycord:bot:setmessageedit", ["Bot", "Procedure|NoneType"], "Setting Function called when a message is edited (or None)")
def lpycord_bot_setmessageedit(args):
    args[0].callbacks["message_edit"] = args[1]

@lispy_function("lpycord:bot:setreactionadd", ["Bot", "Procedure|NoneType"], "Setting Function called when a reaction is added (or None)")
def lpycord_bot_setreactionadd(args):
    args[0].callbacks["reaction_add"] = args[1]

@lispy_function("lpycord:bot:setreactionremove", ["Bot", "Procedure|NoneType"], "Setting Function called when a reaction is removed (or None)")
def lpycord_bot_setreactionremove(args):
    args[0].callbacks["reaction_remove"] = args[1]

@lispy_function("lpycord:bot:setmemberjoin", ["Bot", "Procedure|NoneType"], "Setting Function called when a member join a guild (or None)")
def lpycord_bot_setmemberjoin(args):
    args[0].callbacks["member_join"] = args[1]

@lispy_function("lpycord:bot:setmemberremove", ["Bot", "Procedure|NoneType"], "Setting Function called when a member leave a guild (or None)")
def lpycord_bot_setmemberremove(args):
    args[0].callbacks["member_remove"] = args[1]