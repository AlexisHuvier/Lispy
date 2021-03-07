import discord

class Bot(discord.Client): 
    def __init__(self, prefix):
        super().__init__()
        self.commands = []
        self.prefix = prefix
        self.callbacks = {
            "ready": None,
            "message": None,
            "message_delete": None,
            "message_edit": None,
            "reaction_add": None,
            "reaction_remove": None,
            "member_join": None,
            "member_remove": None
        }

    async def on_ready(self):
        if self.callbacks["ready"] != None:
            self.callbacks["ready"](self)

    async def on_message(self, message):
        if message.author == self.user:
            return

        for i in self.commands:
            if message.content.split(" ")[0] == self.prefix + i.name:
                if i.callback is not None:
                    i.callback(self, message)
                return
        
        if self.callbacks["message"] != None:
            self.callbacks["message"](self, message)
    
    async def on_message_delete(self, message):
        if self.callbacks["message_delete"] != None:
            self.callbacks["message_delete"](self, message)

    async def on_message_edit(self, before, after):
        if self.callbacks["message_edit"] != None:
            self.callbacks["message_edit"](self, before, after)
        
    async def on_reaction_add(self, reaction, user):
        if self.callbacks["reaction_add"] != None:
            self.callbacks["reaction_add"](self, reaction, user)

    async def on_reaction_remove(self, rection, user):
        if self.callbacks["reaction_remove"] != None:
            self.callbacks["reaction_remove"](self, reaction, user)
        
    async def on_member_join(self, member):
        if self.callbacks["member_join"] != None:
            self.callbacks["member_join"](self, member)
        
    async def on_member_remove(self, member):
        if self.callbacks["member_remove"] != None:
            self.callbacks["member_remove"](self, member)

