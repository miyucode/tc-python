from twitchio.ext import commands
import json


class Bot(commands.Bot):
    def __init__(self):
        json_file = open('default_config.json', 'r')
        data = json.load(json_file)
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=data["token"], prefix='?', initial_channels=[data["channel"]])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Hello {self.nick}')

    async def event_message(self, ctx: commands.Context):
        print(f"{ctx.author.name} : {ctx.content}")



bot = Bot()
bot.run()
