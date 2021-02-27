import discord

class Bot(discord.Client): 
    def __init__(self, prefix):
        super().__init__()
        self.commands = []
        self.prefix = prefix

    async def on_ready(self):
        print(self.user, "has connected to Discord.")

    async def on_message(self, message):
        if message.author == self.user:
            return

        for i in self.commands:
            if message.content.split(" ")[0] == self.prefix + i.name:
                if i.callback is not None:
                    i.callback(self, message)
                return

