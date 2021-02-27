from lispy.error import lispy_function


@lispy_function("lpycord:textchan:id", ["TextChannel"], "Getting channel id")
def lpycord_textchan_id(args):
    return args[0].id

@lispy_function("lpycord:textchan:category", ["TextChannel"], "Getting channel category")
def lpycord_textchan_category(args):
    return args[0].category

@lispy_function("lpycord:textchan:name", ["TextChannel"], "Getting channel name")
def lpycord_textchan_name(args):
    return args[0].name

@lispy_function("lpycord:textchan:topic", ["TextChannel"], "Getting channel topic (None if it doesn't exist)")
def lpycord_textchan_topic(args):
    return args[0].topic

@lispy_function("lpycord:textchan:history", ["TextChannel", "int"], "Getting x messages from history of channel", True)
async def lpycord_textchan_history(args):
    return await args[0].history(limit=args[1]).flatten()

@lispy_function("lpycord:textchan:members", ["TextChannel"], "Getting members that can see channel")
def lpycord_textchan_members(args):
    return args[0].members

@lispy_function("lpycord:textchan:isnsfw", ["TextChannel"], "Return if channel is NSFW")
def lpycord_textchan_isnsfw(args):
    return args[0].is_nsfw()

@lispy_function("lpycord:textchan:isnews", ["TextChannel"], "Return if channel is news")
def lpycord_textchan_isnews(args):
    return args[0].is_news()

@lispy_function("lpycord:textchan:clone", ["TextChannel"], "Clone a channel", True)
async def lpycord_textchan_clone(args):
    return await args[0].clone()

@lispy_function("lpycord:textchan:purge", ["TextChannel", "int"], "Delete x message from channel", True)
async def lpycord_textchan_purge(args):
    return await args[0].purge(limit=args[1])

@lispy_function("lpycord:textchan:creation", ["TextChannel"], "Getting creation time of channel")
def lpycord_textchan_creation(args):
    return args[0].created_at

@lispy_function("lpycord:textchan:delete", ["TextChannel"], "Deleting a channel", True)
async def lpycord_textchan_delete(args):
    await args[0].delete()

@lispy_function("lpycord:textchan:mention", ["TextChannel"], "Getting string mention of channel")
def lpycord_textchan_mention(args):
    return args[0].mention

@lispy_function("lpycord:textchan:pins", ["TextChannel"], "Getting pinned messages", True)
async def lpycord_textchan_pins(args):
    return await args[0].pins()

@lispy_function("lpycord:textchan:send", ["TextChannel", "str"], "Sending content", True)
async def lpycord_textchan_send(args):
    await args[0].send(content=args[1])

@lispy_function("lpycord:textchan:sendembed", ["TextChannel", "Embed"], "Sending content", True)
async def lpycord_textchan_sendembed(args):
    await args[0].send(embed=args[1])

@lispy_function("lpycord:textchan:sendfile", ["TextChannel", "str"], "Sending content", True)
async def lpycord_textchan_sendfile(args):
    await args[0].send(file=args[1])