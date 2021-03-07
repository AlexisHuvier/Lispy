from lispy.error import lispy_function


@lispy_function("lpycord:user:name", ["User|ClientUser"], "Getting user's username")
def lpycord_user_name(args):
    return args[0].name

@lispy_function("lpycord:user:id", ["User|ClientUser"], "Getting user's id")
def lpycord_user_id(args):
    return args[0].id

@lispy_function("lpycord:user:discriminator", ["User|ClientUser"], "Getting user's discriminator")
def lpycord_user_discriminator(args):
    return args[0].discriminator

@lispy_function("lpycord:user:avatar", ["User|ClientUser"], "Getting user's avatar")
def lpycord_user_avatar(args):
    return args[0].avatar

@lispy_function("lpycord:user:bot", ["User|ClientUser"], "Returning if user is a bot")
def lpycord_user_bot(args):
    return args[0].bot

@lispy_function("lpycord:user:system", ["User|ClientUser"], "Returning if user is system")
def lpycord_user_system(args):
    return args[0].system

@lispy_function("lpycord:user:creating", ["User|ClientUser"], "Getting user's creation date")
def lpycord_user_creating(args):
    return args[0].created_at

@lispy_function("lpycord:user:mention", ["User|ClientUser"], "Getting user's mention")
def lpycord_user_mention(args):
    return args[0].mention

@lispy_function("lpycord:user:mentionin", ["User|ClientUser", "Message"], "Return if user is mentioned in message")
def lpycord_user_mentionin(args):
    return args[0].mentioned_in(args[0])

@lispy_function("lpycord:user:send", ["User|ClientUser", "str"], "Sending content", True)
async def lpycord_user_send(args):
    await args[0].send(content=args[1])

@lispy_function("lpycord:user:sendembed", ["User|ClientUser", "Embed"], "Sending content", True)
async def lpycord_user_sendembed(args):
    await args[0].send(embed=args[1])

@lispy_function("lpycord:user:sendfile", ["User|ClientUser", "str"], "Sending content", True)
async def lpycord_user_sendfile(args):
    await args[0].send(file=args[1])