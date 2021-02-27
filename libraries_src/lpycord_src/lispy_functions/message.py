from lispy.error import lispy_function


@lispy_function("lpycord:message:author", ["Message"], "Getting message author")
def lpycord_message_author(args):
    return args[0].author

@lispy_function("lpycord:message:id", ["Message"], "Getting message id")
def lpycord_message_id(args):
    return args[0].id

@lispy_function("lpycord:message:content", ["Message"], "Getting message content")
def lpycord_message_content(args):
    return args[0].content

@lispy_function("lpycord:message:cleancontent", ["Message"], "Getting clean message content")
def lpycord_message_cleancontent(args):
    return args[0].clean_content

@lispy_function("lpycord:message:guild", ["Message"], "Getting message guild")
def lpycord_message_guild(args):
    return args[0].guild

@lispy_function("lpycord:message:channel", ["Message"], "Getting message channel")
def lpycord_message_channel(args):
    return args[0].channel

@lispy_function("lpycord:message:type", ["Message"], "Getting message type")
def lpycord_message_type(args):
    return args[0].type

@lispy_function("lpycord:message:pin", ["Message"], "Pin a message", True)
async def lpycord_message_pin(args):
    await args[0].pin()

@lispy_function("lpycord:message:unpin", ["Message"], "Unpin a message", True)
async def lpycord_message_unpin(args):
    await args[0].unpin()

@lispy_function("lpycord:message:delete", ["Message"], "Deleting message", True)
async def lpycord_message_delete(args):
    await args[0].delete()

@lispy_function("lpycord:message:deletedelay", ["Message", "float"], "Deleting message with a delay", True)
async def lpycord_message_deletedelay(args):
    await args[0].delete(delay=args[1])

@lispy_function("lpycord:message:reply", ["Message", "str"], "Reply to a message", True)
async def lpycord_message_reply(args):
    return await args[0].reply(content=args[1])